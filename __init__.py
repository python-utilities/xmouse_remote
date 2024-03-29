#!/usr/bin/env python3


import time

from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input


__license__ = """
Python2/3 mouse wrapper API of `Xlib`
Copyright (C) 2019  S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class XMouse_Remote(object):
    """
    Python2/3 mouse wrapper API of `Xlib`

    - `display` optional if `DISPLAY` environment variable is set
    - `button_ids` optional if satisfied with defaults

    ## Example usage

        mouse = XMouse_Remote()
        print("XMouse_Remote location -> {}".format(mouse.location))

        mouse.move_relative(x = 5, button_name = 'button_left')
        print("XMouse_Remote location -> {}".format(mouse.location))
    """

    def __init__(self, display = None, button_ids = None):
        """
        See -- http://python-xlib.sourceforge.net/doc/html/python-xlib_16.html#SEC15

        - `display`, string of X display address eg. `":0"`
        - `button_ids`, dictionary of key name to detail ID mapping

        ## Example

            mouse = XMouse_Remote(display = ':0', button_ids = {
                'button_left': 1,
                'button_middle': 2,
                'button_right': 3,
                'scroll_up': 4,
                'scroll_down': 5,
                'scroll_left': 6,
                'scroll_right': 7
            })

            print("XMouse_Remote location -> {}".format(mouse.location))
            mouse.drag_relative(y = 5, button_name = 'button_left')
            print("XMouse_Remote location -> {}".format(mouse.location))
        """
        self.display = Display(display)

        self.button_ids = button_ids
        if type(self.button_ids) is not dict:
            self.button_ids = {
                'button_left': 1,
                'button_middle': 2,
                'button_right': 3,
                'scroll_up': 4,
                'scroll_down': 5,
                'scroll_left': 6,
                'scroll_right': 7
            }

        ## For future or super features
        self.relative_constraints = {
            'min_x': -25,
            'max_x': 25,
            'min_y': -25,
            'max_y': 25
        }
        ## Zero and positive integers on most displays
        self.absolute_constraints = {
            'min_x': 0,
            'max_x': self.display.screen().width_in_pixels,
            'min_y': 0,
            'max_y': self.display.screen().height_in_pixels
        }

    @property
    def location(self):
        """
        Returns `[x, y]` list of coordinates that mouse cursor occupies

        ## Example

            print("Mouse location -> {}".format(mouse.location))
        """
        _coordinates = self.display.screen().root.query_pointer()._data
        return [_coordinates.get('root_x'), _coordinates.get('root_y')]

    def button_click(self, detail = 1, button_name = None, times = 1, sync = True, delays = {0: 0.01}):
        """
        Calls `self.button_press(...)` then `self.button_release(...)` a number of `times`

        - `detail` default `detail = 1`, or `button_name` may be used to select a given button
        - `times` number of times to press and release provided `detail` or `button_name`
        - `sync` default `sync = True`, triggers `self.display.sync()` if `True`
        - `delays` dictionary default `{0: 0.01}`, seconds to `time.sleep(<n>)` for

        ## Example

            mouse.button_click(detail = 1, times = 2, delays = {0: 0.05})
        """
        for _ in range(times):
            self.button_press(detail = detail, button_name = button_name, sync = sync)

            if delays.get(0, 0) > 0:
                time.sleep(delays[0])

            self.button_release(detail = detail, button_name = button_name, sync = sync)

    def button_press(self, detail = 1, button_name = None, sync = True):
        """
        Presses detailed button name

        - `detail` default `detail = 1`, or `button_name` may be used to press a given button
        - `sync` default `sync = True`, triggers `self.display.sync()` if `True`

        ## Example

            mouse.button_press(detail = 1)
            time.sleep(0.02)
            mouse.move_relative(y = -5)
            mouse.button_release(detail = 1)
        """
        _target_id = detail
        if button_name is not None:
            _target_id = self.button_ids.get(button_name, 1)

        fake_input(self.display, event_type = X.ButtonPress, detail = _target_id)

        if sync:
            self.display.sync()

    def button_release(self, detail = 1, button_name = None, sync = True):
        """
        Releases detailed button name

        - `detail` default `detail = 1`, or `button_name` may be used to release a given button
        - `sync` default `sync = True`, triggers `self.display.sync()` if `True`

        ## Example

            mouse.button_press(detail = 1)
            time.sleep(0.02)
            mouse.move_relative(y = -5)
            mouse.button_release(detail = 1)
        """
        _target_id = detail
        if button_name is not None:
            _target_id = self.button_ids.get(button_name, 1)

        fake_input(self.display, event_type = X.ButtonRelease, detail = detail)

        if sync:
            self.display.sync()

    def drag_absolute(self, x, y, detail = 1, button_name = None, sync = True, delays = {0: 0.01, 1: 0.01}):
        """
        Starting at `self.location`, moves to absolute coordinates while pressing defined button ID or name

        - `x` and `y` are passed to `self.move_absolute(...)` after `self.button_press(...)`
        - `detail` default `detail = 1`, or `button_name` may be used to press and release a button
        - `sync` default `sync = True`, triggers `self.display.sync()` if `True`
        - `delays` default `{0: 0.01, 1: 0.01}`, `time.sleep(<n>)` before and after `self.move_absolute(...)`

        ## Example

            mouse.move_absolute(x = 0, y = 0)
            mouse.drag_absolute(x = 10, y = 20, detail = 1)
        """
        self.button_press(detail = detail, button_name = button_name, sync = sync)

        if delays.get(0, 0) > 0:
            time.sleep(delays[0])

        self.move_absolute(x = x, y = y, sync = sync)

        if delays.get(1, 0) > 0:
            time.sleep(delays[1])

        self.button_release(detail = _target_id, sync = sync)

        return self.location

    def drag_relative(self, x = 0, y = 0, detail = 1, button_name = None, sync = True, delays = {0: 0.01, 1: 0.01}):
        """
        Starting at `self.location`, moves to relative coordinates while pressing defined button ID or name

        - `x` and `y` are passed to `self.move_relative(...)` after `self.button_press(...)`
        - `detail` default `detail = 1`, or `button_name` may be used to press and release a button
        - `sync` default `sync = True`, triggers `self.display.sync()` if `True`
        - `delays` default `{0: 0.01, 1: 0.01}`, `time.sleep(<n>)` before and after `self.move_relative(...)`

        ## Example

            mouse.drag_relative(x = 5, y = -10, detail = 1)
        """
        self.button_press(detail = detail, button_name = button_name, sync = sync)

        if delays.get(0, 0) > 0:
            time.sleep(delays[0])

        self.move_relative(x = x, y = y, sync = sync)

        if delays.get(1, 0) > 0:
            time.sleep(delays[1])

        self.button_release(detail = detail, button_name = button_name, sync = sync)

        return self.location

    def move_absolute(self, x, y, sync = True):
        """
        Returns `self.location` after telaporting mouse to `x` and `y` coordinates

        See -- https://github.com/python-xlib/python-xlib/blob/master/Xlib/ext/xtest.py

        - `x` horizontal coordinate, usually `0` to `self.display.screen().width_in_pixels`
        - `y` vertical coordinate, usually `0` to `self.display.screen().height_in_pixels`
        - `sync` if `True` will call `self.display.sync()` prior to returning `self.location`

        ## Example

            mouse.move_absolute(x = 0, y = 0)
        """
        fake_input(self.display, event_type = X.MotionNotify, x = x, y = y)

        if sync:
            self.display.sync()

        return self.location

    def move_relative(self, x = 0, y = 0, sync = True):
        """
        Returns `self.location` after moving relative distance from current mouse coordinates

        - `x` if negative moves mouse Left, and if positive moves mouse Right
        - `y` if negative moves mouse Up, and if positive moves mouse Down
        - `sync` if `True` will call `self.display.sync()` prior to returning `self.location`

        ## Example

            mouse.move_relative(x = 5, y = -10)
        """
        _new_location = self.location

        if x != 0:
            _new_location[0] = _new_location[0] + x

        if y != 0:
            _new_location[1] = _new_location[1] + y

        return self.move_absolute(*_new_location, sync = sync)

    def scroll(self, x = 0, y = 0):
        """
        Scroll up or left if positive and down or right if negative

        - `x` if negative scrolls columns Left, and if positive scrolls columns Right
        - `y` if negative scrolls rows Up, and if positive scrolls rows Down

        ## Example

            mouse.scroll(x = 5, y = -10)
        """
        if y > 0:
            self.button_click(detail = self.button_ids.get('scroll_up', 4), times = y)
        elif y < 0:
            self.button_click(detail = self.button_ids.get('scroll_down', 5), times = abs(y))

        if x > 0:
            self.button_click(detail = self.button_ids.get('scroll_left', 6), times = x)
        elif x < 0:
            self.button_click(detail = self.button_ids.get('scroll_right', 7), times = abs(x))
