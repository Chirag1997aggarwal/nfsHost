#!/bin/sh
echo "Creating an LVM of size - $1"
echo "name of LVM is $2"

lvcreate -L $1M -n $2 nfsHub -y
echo "lv created"
mkfs.ext4 /dev/nfsHub/$2 -F
echo "filesystem formatted"
mkdir -p /nfs/dir/$2
echo "created mount dir"
mount /dev/nfsHub/$2 /nfs/dir/$2
echo "mount dir with lv"
chown nobody:nogroup /nfs/dir/$2
echo "set nobody:nogroup"
echo "system client IP - $3"
echo "/nfs/dir/$2	$3(rw,sync,no_subtree_check)" >> /etc/exports
echo "made entry in  etc/exports file"
systemctl restart nfs-kernel-server
echo "nfs kernel restarted"
