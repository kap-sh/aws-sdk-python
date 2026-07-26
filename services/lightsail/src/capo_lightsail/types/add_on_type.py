"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnType``."""

from typing import Literal, TypeAlias, cast

AddOnType: TypeAlias = Literal[
    "AutoSnapshot",
    "StopInstanceOnIdle",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddOnType:
    return cast(AddOnType, data)
