"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Dimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

Dimension: TypeAlias = Literal[
    "SavingsValue",
    "SavingsValueAfterDiscount",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SavingsValue",
        "SavingsValueAfterDiscount",
    )
)


def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)
