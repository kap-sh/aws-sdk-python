"""Generated from Smithy shape ``com.amazonaws.s3vectors#NonFilterableMetadataKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.metadata_key

NonFilterableMetadataKeys: TypeAlias = list[
    "capo_s3vectors.types.metadata_key.MetadataKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: NonFilterableMetadataKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> NonFilterableMetadataKeys:
    return list(data)
