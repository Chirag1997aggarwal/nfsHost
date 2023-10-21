from flask import Flask, render_template, request, jsonify
import socket
import subprocess
from subprocess import Popen, PIPE
import uuid

from utils import runShellCmd, setClient


app = Flask(__name__) 

@app.route("/")
def base_url():
    return render_template("index.html")

@app.route("/create_mount_nfs")
def create_mount_nfs():
    data = request.args.to_dict()
    
    lv_name = str(uuid.uuid4())
    print('uuid', lv_name)

    runShellCmd(['./nfs/createLvm.sh', data['size'], lv_name, data['clientIP']])
    #runShellCmd(['./nfs/setClient.sh', data['clientIP'], data['user'], data['pswd'], lv_name])

    hostname = socket.gethostname()
    print('hostName', hostname)
    hostIP = [l for l in ([ip for ip in socket.gethostbyname_ex(hostname)[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    print('hostIP', hostIP)
    setClient(data['clientIP'], data['user'], data['pswd'], lv_name, hostIP)
    #runShellCmd(['./nfs/createLvm.sh'])
    print(data)
    return f"LV created and mounted successfully. Shared file system path -/nfs/dir/{lv_name}"

if __name__ == "__main__":
    app.run(debug=True, port=8001, host='0.0.0.0')
