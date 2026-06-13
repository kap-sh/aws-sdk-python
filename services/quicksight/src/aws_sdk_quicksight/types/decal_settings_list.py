"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decal_settings

DecalSettingsList: TypeAlias = list[
    "aws_sdk_quicksight.types.decal_settings.DecalSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecalSettingsList) -> list:
    import aws_sdk_quicksight.types.decal_settings

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.decal_settings.serialize_json(item))
    return out


def deserialize_json(data: list) -> DecalSettingsList:
    import aws_sdk_quicksight.types.decal_settings

    out: DecalSettingsList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.decal_settings.deserialize_json(item))
    return out
