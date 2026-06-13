"""Generated from Smithy shape ``com.amazonaws.datazone#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_key
    import aws_sdk_datazone.types.metadata_value

Metadata: TypeAlias = dict[
    "aws_sdk_datazone.types.metadata_key.MetadataKey",
    "aws_sdk_datazone.types.metadata_value.MetadataValue",
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
