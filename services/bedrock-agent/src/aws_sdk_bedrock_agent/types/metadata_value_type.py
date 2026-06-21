"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataValueType``."""

from typing import Literal, TypeAlias, cast

MetadataValueType: TypeAlias = Literal[
    "BOOLEAN",
    "NUMBER",
    "STRING",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataValueType) -> str:
    return value


def deserialize_json(data: str) -> MetadataValueType:
    return cast(MetadataValueType, data)
