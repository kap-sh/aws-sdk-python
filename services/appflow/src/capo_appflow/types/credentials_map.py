"""Generated from Smithy shape ``com.amazonaws.appflow#CredentialsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.credentials_map_key
    import capo_appflow.types.credentials_map_value

CredentialsMap: TypeAlias = dict[
    "capo_appflow.types.credentials_map_key.CredentialsMapKey",
    "capo_appflow.types.credentials_map_value.CredentialsMapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CredentialsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CredentialsMap:
    out: CredentialsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
