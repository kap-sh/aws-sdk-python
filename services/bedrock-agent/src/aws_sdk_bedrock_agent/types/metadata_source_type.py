"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataSourceType``."""

from typing import Literal, TypeAlias, cast

MetadataSourceType: TypeAlias = Literal[
    "IN_LINE_ATTRIBUTE",
    "S3_LOCATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataSourceType) -> str:
    return value


def deserialize_json(data: str) -> MetadataSourceType:
    return cast(MetadataSourceType, data)
