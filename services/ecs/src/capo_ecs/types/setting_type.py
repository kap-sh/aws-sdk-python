"""Generated from Smithy shape ``com.amazonaws.ecs#SettingType``."""

from typing import Literal, TypeAlias, cast

SettingType: TypeAlias = Literal[
    "user",
    "aws_managed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingType:
    return cast(SettingType, data)
