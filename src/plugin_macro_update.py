#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Run this script to update legacy pluginlib macros to utilize new
# simplified PLUGINLIB_EXPORT_CLASS macro.

import subprocess

cmd = "find . -type f ! -name '*.svn-base' -a ! -name '*.hg' -a ! -name '*.git' -a \( -name '*.c*' -o -name '*.h*' \) -exec sed -i '%(rule)s' {} \;"

rules = ['s/PLUGINLIB_DECLARE_CLASS(.*,.*,\(.*\),\(.*\))/PLUGINLIB_EXPORT_CLASS(\\1,\\2)/g',
         's/PLUGINLIB_REGISTER_CLASS(.*,\(.*\),\(.*\))/PLUGINLIB_EXPORT_CLASS(\\1,\\2)/g',   
        ]

for rule in rules:
    full_cmd = cmd%locals()
    print ("Running %s"%full_cmd)
    ret_code = subprocess.call(full_cmd, shell=True)
    if ret_code == 0:
        print ("success")
    else:
        print ("failure")
