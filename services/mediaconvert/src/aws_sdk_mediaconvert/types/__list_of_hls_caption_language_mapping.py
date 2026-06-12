"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHlsCaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.hls_caption_language_mapping

__listOfHlsCaptionLanguageMapping: TypeAlias = list[
    "aws_sdk_mediaconvert.types.hls_caption_language_mapping.HlsCaptionLanguageMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsCaptionLanguageMapping) -> list:
    import aws_sdk_mediaconvert.types.hls_caption_language_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.hls_caption_language_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfHlsCaptionLanguageMapping:
    import aws_sdk_mediaconvert.types.hls_caption_language_mapping

    out: __listOfHlsCaptionLanguageMapping = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.hls_caption_language_mapping.deserialize_json(
                item
            )
        )
    return out
