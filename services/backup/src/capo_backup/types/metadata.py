"""Generated from Smithy shape ``com.amazonaws.backup#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.metadata_key
    import capo_backup.types.metadata_value

Metadata: TypeAlias = dict[
    "capo_backup.types.metadata_key.MetadataKey",
    "capo_backup.types.metadata_value.MetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        out[key] = value
    return out
