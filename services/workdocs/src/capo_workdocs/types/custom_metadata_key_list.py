"""Generated from Smithy shape ``com.amazonaws.workdocs#CustomMetadataKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.custom_metadata_key_type

CustomMetadataKeyList: TypeAlias = list[
    "capo_workdocs.types.custom_metadata_key_type.CustomMetadataKeyType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetadataKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomMetadataKeyList:
    return list(data)
