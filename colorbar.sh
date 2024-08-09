#!/bin/bash
ffmpeg -f lavfi -i smpteh -t 3600 -vf "scale=1920:1080" -f v4l2 /dev/video0
