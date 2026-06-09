"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityOptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityOptionType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
    "RESERVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SPOT",
        "RESERVED",
    )
)


def serialize_aws_json_1_1(value: CapacityOptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityOptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityOptionType value: {data!r}")
    return cast(CapacityOptionType, data)
