"""Generated from Smithy shape ``com.amazonaws.batch#CRAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

CRAllocationStrategy: TypeAlias = Literal[
    "BEST_FIT",
    "BEST_FIT_PROGRESSIVE",
    "SPOT_CAPACITY_OPTIMIZED",
    "SPOT_PRICE_CAPACITY_OPTIMIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CRAllocationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CRAllocationStrategy:
    return cast(CRAllocationStrategy, data)
