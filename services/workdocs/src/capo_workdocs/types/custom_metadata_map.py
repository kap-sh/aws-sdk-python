"""Generated from Smithy shape ``com.amazonaws.workdocs#CustomMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.custom_metadata_key_type
    import capo_workdocs.types.custom_metadata_value_type

CustomMetadataMap: TypeAlias = dict[
    "capo_workdocs.types.custom_metadata_key_type.CustomMetadataKeyType",
    "capo_workdocs.types.custom_metadata_value_type.CustomMetadataValueType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomMetadataMap:
    out: CustomMetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
