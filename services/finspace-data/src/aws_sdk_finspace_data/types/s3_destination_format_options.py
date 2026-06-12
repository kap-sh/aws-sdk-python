"""Generated from Smithy shape ``com.amazonaws.finspacedata#S3DestinationFormatOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_map_key
    import aws_sdk_finspace_data.types.string_map_value

S3DestinationFormatOptions: TypeAlias = dict[
    "aws_sdk_finspace_data.types.string_map_key.StringMapKey",
    "aws_sdk_finspace_data.types.string_map_value.StringMapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: S3DestinationFormatOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> S3DestinationFormatOptions:
    out: S3DestinationFormatOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
