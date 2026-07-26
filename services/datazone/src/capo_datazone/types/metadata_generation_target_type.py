"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationTargetType``."""

from typing import Literal, TypeAlias, cast

MetadataGenerationTargetType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationTargetType) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationTargetType:
    return cast(MetadataGenerationTargetType, data)
