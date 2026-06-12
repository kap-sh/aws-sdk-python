"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskTimeoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

DecisionTaskTimeoutType: TypeAlias = Literal[
    "START_TO_CLOSE",
    "SCHEDULE_TO_START",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_TO_CLOSE",
        "SCHEDULE_TO_START",
    )
)


def serialize_aws_json_1_0(value: DecisionTaskTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DecisionTaskTimeoutType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecisionTaskTimeoutType value: {data!r}")
    return cast(DecisionTaskTimeoutType, data)
