"""Generated from Smithy shape ``com.amazonaws.backup#ResourceTypeOptInPreference``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.is_enabled
    import capo_backup.types.resource_type

ResourceTypeOptInPreference: TypeAlias = dict[
    "capo_backup.types.resource_type.ResourceType",
    "capo_backup.types.is_enabled.IsEnabled",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceTypeOptInPreference) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceTypeOptInPreference:
    out: ResourceTypeOptInPreference = {}
    for key, value in data.items():
        out[key] = value
    return out
