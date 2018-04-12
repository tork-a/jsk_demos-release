#!/bin/bash

MAP=eng2
#MAP=scene1

if [ -n "$1" ]; then
    MAP=$1
fi

rosrun roseus roseus `rospack find jsk_maps`/tools/convert-iasmap.l "(progn (yaml :$MAP) (exit))"

rosrun jsk_maps yaml2owl.py $MAP.yaml > $MAP.owl.in

# remove temporary yaml file
rm $MAP.yaml
