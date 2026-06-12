"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.tag_key
    import aws_sdk_kinesis_video.types.tag_value

ResourceTags: TypeAlias = dict[
    "aws_sdk_kinesis_video.types.tag_key.TagKey",
    "aws_sdk_kinesis_video.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceTags:
    out: ResourceTags = {}
    for key, value in data.items():
        out[key] = value
    return out
