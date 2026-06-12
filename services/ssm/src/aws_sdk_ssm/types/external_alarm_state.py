"""Generated from Smithy shape ``com.amazonaws.ssm#ExternalAlarmState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ExternalAlarmState: TypeAlias = Literal[
    "UNKNOWN",
    "ALARM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "ALARM",
    )
)


def serialize_aws_json_1_1(value: ExternalAlarmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExternalAlarmState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalAlarmState value: {data!r}")
    return cast(ExternalAlarmState, data)
