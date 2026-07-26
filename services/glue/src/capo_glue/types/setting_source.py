"""Generated from Smithy shape ``com.amazonaws.glue#SettingSource``."""

from typing import Literal, TypeAlias, cast

SettingSource: TypeAlias = Literal[
    "CATALOG",
    "TABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingSource:
    return cast(SettingSource, data)
