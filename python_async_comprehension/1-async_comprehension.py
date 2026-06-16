#!/usr/bin/env python3
"""Module that import async_generator"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous comprehension that collect and return
     a random  number between 0 and 10"""
    return [n async for n in async_generator()]
