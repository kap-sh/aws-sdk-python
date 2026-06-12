"""Generated from Smithy shape ``com.amazonaws.wickr#SettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.setting

SettingsList: TypeAlias = list["aws_sdk_wickr.types.setting.Setting"]


# --- restJson1 ser/de ---
def serialize_json(value: SettingsList) -> list:
    import aws_sdk_wickr.types.setting

    out: list = []
    for item in value:
        out.append(aws_sdk_wickr.types.setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> SettingsList:
    import aws_sdk_wickr.types.setting

    out: SettingsList = []
    for item in data:
        out.append(aws_sdk_wickr.types.setting.deserialize_json(item))
    return out
