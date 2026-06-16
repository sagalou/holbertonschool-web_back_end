#!/usr/bin/env python3
"""Module that calls async_generator"""


import asyncio
import random


async def async_generator():
    """Asynchronous generator that waits 1 second and yields
     a random  number between 0 and 10, repeated 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        delay: float = random.uniform(0, 10)
        yield delay
