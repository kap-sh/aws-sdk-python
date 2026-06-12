"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

AllocationStrategy: TypeAlias = Literal[
    "Prioritized",
    "LowestPrice",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Prioritized",
        "LowestPrice",
    )
)


def serialize_aws_json_1_0(value: AllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllocationStrategy value: {data!r}")
    return cast(AllocationStrategy, data)
