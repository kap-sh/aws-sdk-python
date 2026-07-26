"""Generated from Smithy shape ``com.amazonaws.ssm#ExternalAlarmState``."""

from typing import Literal, TypeAlias, cast

ExternalAlarmState: TypeAlias = Literal[
    "UNKNOWN",
    "ALARM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalAlarmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExternalAlarmState:
    return cast(ExternalAlarmState, data)
