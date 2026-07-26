"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedResultRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.supported_s3_region

AllowedResultRegions: TypeAlias = list[
    "capo_cleanrooms.types.supported_s3_region.SupportedS3Region"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedResultRegions) -> list:
    import capo_cleanrooms.types.supported_s3_region

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.supported_s3_region.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedResultRegions:
    import capo_cleanrooms.types.supported_s3_region

    out: AllowedResultRegions = []
    for item in data:
        out.append(capo_cleanrooms.types.supported_s3_region.deserialize_json(item))
    return out
