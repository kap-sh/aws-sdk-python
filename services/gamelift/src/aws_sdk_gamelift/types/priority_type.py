"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PriorityType: TypeAlias = Literal[
    "LATENCY",
    "COST",
    "DESTINATION",
    "LOCATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATENCY",
        "COST",
        "DESTINATION",
        "LOCATION",
    )
)


def serialize_aws_json_1_1(value: PriorityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PriorityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PriorityType value: {data!r}")
    return cast(PriorityType, data)
