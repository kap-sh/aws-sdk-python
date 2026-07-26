"""Generated from Smithy shape ``com.amazonaws.backup#GlobalSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.global_settings_name
    import capo_backup.types.global_settings_value

GlobalSettings: TypeAlias = dict[
    "capo_backup.types.global_settings_name.GlobalSettingsName",
    "capo_backup.types.global_settings_value.GlobalSettingsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GlobalSettings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> GlobalSettings:
    out: GlobalSettings = {}
    for key, value in data.items():
        out[key] = value
    return out
