"""Generated from Smithy shape ``com.amazonaws.ecs#BurstablePerformance``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

BurstablePerformance: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "included",
        "required",
        "excluded",
    )
)


def serialize_aws_json_1_1(value: BurstablePerformance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BurstablePerformance:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurstablePerformance value: {data!r}")
    return cast(BurstablePerformance, data)
