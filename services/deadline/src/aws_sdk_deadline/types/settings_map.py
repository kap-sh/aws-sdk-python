"""Generated from Smithy shape ``com.amazonaws.deadline#SettingsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.setting_key
    import aws_sdk_deadline.types.setting_value

SettingsMap: TypeAlias = dict[
    "aws_sdk_deadline.types.setting_key.SettingKey",
    "aws_sdk_deadline.types.setting_value.SettingValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SettingsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SettingsMap:
    out: SettingsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
