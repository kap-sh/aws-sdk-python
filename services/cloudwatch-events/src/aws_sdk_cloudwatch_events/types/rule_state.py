"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RuleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

RuleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: RuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleState value: {data!r}")
    return cast(RuleState, data)
