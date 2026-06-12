"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsRuntimeMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string
    import aws_sdk_chime_sdk_media_pipelines.types.string

MediaInsightsRuntimeMetadata: TypeAlias = dict[
    "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
    "aws_sdk_chime_sdk_media_pipelines.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MediaInsightsRuntimeMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MediaInsightsRuntimeMetadata:
    out: MediaInsightsRuntimeMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
