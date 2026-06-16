#!/usr/bin/env python3
"""Module that import async_comprehension"""


import asyncio
import time


from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel using
    asyncio.gather, measure the total runtime, and return it"""
    debut = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.perf_counter() - debut
    return total_time
