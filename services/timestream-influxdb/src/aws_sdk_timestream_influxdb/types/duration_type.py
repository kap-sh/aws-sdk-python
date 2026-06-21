"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DurationType``."""

from typing import Literal, TypeAlias, cast

DurationType: TypeAlias = Literal[
    "hours",
    "minutes",
    "seconds",
    "milliseconds",
    "days",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DurationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DurationType:
    return cast(DurationType, data)
