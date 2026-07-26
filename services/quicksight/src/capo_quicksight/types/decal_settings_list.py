"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.decal_settings

DecalSettingsList: TypeAlias = list[
    "capo_quicksight.types.decal_settings.DecalSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecalSettingsList) -> list:
    import capo_quicksight.types.decal_settings

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.decal_settings.serialize_json(item))
    return out


def deserialize_json(data: list) -> DecalSettingsList:
    import capo_quicksight.types.decal_settings

    out: DecalSettingsList = []
    for item in data:
        out.append(capo_quicksight.types.decal_settings.deserialize_json(item))
    return out
