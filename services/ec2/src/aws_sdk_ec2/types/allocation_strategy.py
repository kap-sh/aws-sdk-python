"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationStrategy``."""

from typing import Literal, TypeAlias

AllocationStrategy: TypeAlias = Literal[
    "lowestPrice",
    "diversified",
    "capacityOptimized",
    "capacityOptimizedPrioritized",
    "priceCapacityOptimized",
]
