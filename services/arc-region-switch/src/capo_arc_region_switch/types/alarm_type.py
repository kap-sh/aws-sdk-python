"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AlarmType``."""

from typing import Literal, TypeAlias, cast

AlarmType: TypeAlias = Literal[
    "applicationHealth",
    "trigger",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmType:
    return cast(AlarmType, data)
