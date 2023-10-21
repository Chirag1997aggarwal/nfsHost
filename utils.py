import subprocess
from subprocess import Popen, PIPE


def runShellCmd(cmd):
	
	
	session = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
	
	stdout, stderr = session.communicate()
	
	print('output', stdout.splitlines())
	#print('err', stderr)
	if stderr != b'':
		print('Err while running', cmd)
		print('Err -', stderr)
	return stdout

#echo "/nfs/dir/$2       $3(rw,sync,no_subtree_check)" >> /etc/exports
#cript="mkdir -p /nfs/dir/$4 | mount $hostIP:/nfs/dir/$4 /nfs/dir/$4"
def setClient(clientIP, user, pwd, lv_name, hostIP):
	p_mount_str = f'{hostIP}:/nfs/dir/{lv_name} /nfs/dir/{lv_name} nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0'
	command = [
	f"sshpass", "-p", pwd,
	"ssh", "-o", "stricthostkeychecking=no",
	f"{user}@{clientIP}",
	f"echo '{pwd}' | sudo -S mkdir -p /nfs/dir/{lv_name}",
	f"echo '{pwd}' | sudo -S mount -t nfs {hostIP}:/nfs/dir/{lv_name} /nfs/dir/{lv_name}",
	
	#f"sudo -S <<< {pwd} echo  '{p_mount_str}' >> /etc/fstab"
	]

	#command = ['ls', '-la']
	print(command)

	return runShellCmd(command)

