"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelStatus``."""

from typing import Literal, TypeAlias, cast

FlywheelStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlywheelStatus:
    return cast(FlywheelStatus, data)
