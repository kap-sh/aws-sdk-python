"""Generated from Smithy shape ``com.amazonaws.eventbridge#RuleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

RuleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS",
    )
)


def serialize_aws_json_1_1(value: RuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleState value: {data!r}")
    return cast(RuleState, data)
