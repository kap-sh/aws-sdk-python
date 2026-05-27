"""Generated from Smithy shape ``com.amazonaws.ec2#SpotAllocationStrategy``."""

from typing import Literal, TypeAlias

SpotAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "diversified",
    "capacity-optimized",
    "capacity-optimized-prioritized",
    "price-capacity-optimized",
]
