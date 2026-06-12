"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PlacementConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

PlacementConstraintType: TypeAlias = Literal[
    "distinctInstance",
    "memberOf",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "distinctInstance",
        "memberOf",
    )
)


def serialize_aws_json_1_1(value: PlacementConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementConstraintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlacementConstraintType value: {data!r}")
    return cast(PlacementConstraintType, data)
