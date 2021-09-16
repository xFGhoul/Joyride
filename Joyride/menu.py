"""
MIT License

Copyright (c) 2021, Ghoul

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
"""


from abc import ABC, abstractmethod
from typing import List

from .joyride import Joyride


class Interactable(ABC):
    @abstractmethod
    async def prompt():
        pass


class Menu:
    def __init__(self, joyride: Joyride):
        self.joyride = joyride

    async def add_question(self, title: str, message: str, hide_answer: bool, validate):
        pass

    async def add_checkbox(
        self, title: str, message: str, options: List[str], defaults: List[str]
    ):
        pass

    async def add_dropdown(self, title: str, message: str, options: List[str]):
        pass

    async def add_confirm(self, title: str, message: str, default: bool):
        pass

    async def quit(self):
        pass
