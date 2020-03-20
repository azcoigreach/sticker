#!/bin/sh

tmux new-session -d -s sticker 'exec htop'
tmux rename-window 'sticker'
tmux select-window -t sticker:0
tmux split-window -v 'exec python3 sticker.py --symbol ^dji'
tmux split-window -h -t 1 'exec python3 sticker-scroll.py --memo ">>"'
tmux -2 attach-session -t sticker