#!/bin/bash
remote="$1"
user="$2"
pwd="$3"

hostIP=$(hostname -I | cut -d ' ' -f1)
echo "host ip - $hostIP"
script="mkdir -p /nfs/dir/$4 | mount $hostIP:/nfs/dir/$4 /nfs/dir/$4"

sshpass -p $pwd ssh $user@$remote $script
exit
