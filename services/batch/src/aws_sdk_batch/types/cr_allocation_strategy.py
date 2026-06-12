"""Generated from Smithy shape ``com.amazonaws.batch#CRAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CRAllocationStrategy: TypeAlias = Literal[
    "BEST_FIT",
    "BEST_FIT_PROGRESSIVE",
    "SPOT_CAPACITY_OPTIMIZED",
    "SPOT_PRICE_CAPACITY_OPTIMIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEST_FIT",
        "BEST_FIT_PROGRESSIVE",
        "SPOT_CAPACITY_OPTIMIZED",
        "SPOT_PRICE_CAPACITY_OPTIMIZED",
    )
)


def serialize_json(value: CRAllocationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CRAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CRAllocationStrategy value: {data!r}")
    return cast(CRAllocationStrategy, data)
