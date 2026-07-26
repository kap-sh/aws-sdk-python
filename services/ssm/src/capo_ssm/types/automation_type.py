"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationType``."""

from typing import Literal, TypeAlias, cast

AutomationType: TypeAlias = Literal[
    "CrossAccount",
    "Local",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationType:
    return cast(AutomationType, data)
