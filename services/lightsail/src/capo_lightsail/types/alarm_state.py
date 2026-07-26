"""Generated from Smithy shape ``com.amazonaws.lightsail#AlarmState``."""

from typing import Literal, TypeAlias, cast

AlarmState: TypeAlias = Literal[
    "OK",
    "ALARM",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlarmState:
    return cast(AlarmState, data)
