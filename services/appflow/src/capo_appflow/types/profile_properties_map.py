"""Generated from Smithy shape ``com.amazonaws.appflow#ProfilePropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.profile_property_key
    import capo_appflow.types.profile_property_value

ProfilePropertiesMap: TypeAlias = dict[
    "capo_appflow.types.profile_property_key.ProfilePropertyKey",
    "capo_appflow.types.profile_property_value.ProfilePropertyValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ProfilePropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ProfilePropertiesMap:
    out: ProfilePropertiesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
