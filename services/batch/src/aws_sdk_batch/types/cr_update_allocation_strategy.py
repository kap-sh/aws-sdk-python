"""Generated from Smithy shape ``com.amazonaws.batch#CRUpdateAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CRUpdateAllocationStrategy: TypeAlias = Literal[
    "BEST_FIT_PROGRESSIVE",
    "SPOT_CAPACITY_OPTIMIZED",
    "SPOT_PRICE_CAPACITY_OPTIMIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEST_FIT_PROGRESSIVE",
        "SPOT_CAPACITY_OPTIMIZED",
        "SPOT_PRICE_CAPACITY_OPTIMIZED",
    )
)


def serialize_json(value: CRUpdateAllocationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CRUpdateAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CRUpdateAllocationStrategy value: {data!r}"
        )
    return cast(CRUpdateAllocationStrategy, data)
