#!/usr/bin/env python3

# Copyright (c) 2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Tell Cozmo to roll a cube that is placed in front of him.

This example demonstrates Cozmo driving to and rolling a cube.
You must place a cube in front of Cozmo so that he can see it.
'''

import cozmo

async def roll_a_cube(robot: cozmo.robot.Robot):
    print("Cozmo is waiting until he sees a cube")

    cube = await robot.world.wait_for_observed_light_cube()
    
    # Cozmo will approach the cube he has seen and roll it
    # check_for_object_on_top=True enforces that Cozmo will not roll cubes with anything on top
    await robot.roll_cube( cube, check_for_object_on_top=True, num_retries=2 ).wait_for_completed()

cozmo.run_program(roll_a_cube)
