"""Generated from Smithy shape ``com.amazonaws.pcs#SpotAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

SpotAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "capacity-optimized",
    "price-capacity-optimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowest-price",
        "capacity-optimized",
        "price-capacity-optimized",
    )
)


def serialize_aws_json_1_0(value: SpotAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpotAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpotAllocationStrategy value: {data!r}")
    return cast(SpotAllocationStrategy, data)
