#!/usr/bin/env bash

cp -r $SOURCE_DIRECTORY/$EXAMPLE_DIR/* $CYLC_TASK_WORK_DIR
$CORE_ROOT_DIR/bin/tweak_iodef
$LAUNCH_SCRIPT/launch-exe
