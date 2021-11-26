"""
MIT License
Copyright (c) 2021 Marcelo Jacinto
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@author: Marcelo Fialho Jacinto
@email: marcelo.jacinto@tecnico.ulisboa.pt
@date: 25/11/2021
@licence: MIT
"""
from joystick_controller import ControlAssignment
import time

def main():
    
    # Create a configurations dictionary, where a set of buttons, d-pad and analog joysticks
    # are mapped to a given variable.
    button_assingment = {"surge": {"inputs":[
                                        {"type": "axis", "id": 1, "gain": -0.5, "offset": 0.0},
                                        {"type": "hat", "id": 0, "index": 1, "gain": 0.5, "offset": 0.0}],
                                    "integrate": False},

                        "depth": {"inputs":[
                                        {"type": "axis", "id": 2, "gain": -0.5, "offset": 1.0},
                                        {"type": "button", "id": 4, "gain": 0.5, "offset": 0.0}],
                                    "integrate": True,
                                    "lower_limit": -3,
                                    "upper_limit": 0}}


    # Create a joystick controller
    joystick_controller = ControlAssignment(button_assingment)

    # Enter the infinite loop
    while(True):

        # Get a dictionary with the output of the controller (keys will be "surge" and "depth")
        output = joystick_controller.check_events()

        # Print the output dictionary to the screen
        print(output)

        # Sleep for a few milliseconds
        time.sleep(1.0 / 10.0)


if __name__ == '__main__':
    main()