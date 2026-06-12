"""Generated from Smithy shape ``com.amazonaws.gamelift#ZeroCapacityStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ZeroCapacityStrategy: TypeAlias = Literal[
    "MANUAL",
    "SCALE_TO_AND_FROM_ZERO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "SCALE_TO_AND_FROM_ZERO",
    )
)


def serialize_aws_json_1_1(value: ZeroCapacityStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ZeroCapacityStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ZeroCapacityStrategy value: {data!r}")
    return cast(ZeroCapacityStrategy, data)
