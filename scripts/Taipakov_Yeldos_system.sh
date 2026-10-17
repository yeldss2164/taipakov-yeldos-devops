#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="

cat Taipakov_Yeldos_info.txt

echo "=============================="
echo "System Information"
echo "=============================="

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -a)"

echo "Disk Usage:"
df -h /

echo "Memory Usage:"
free -h

echo "=============================="

if [ -f Taipakov_Yeldos_info.txt ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
