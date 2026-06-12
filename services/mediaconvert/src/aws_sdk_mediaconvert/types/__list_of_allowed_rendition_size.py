"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfAllowedRenditionSize``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.allowed_rendition_size

__listOfAllowedRenditionSize: TypeAlias = list[
    "aws_sdk_mediaconvert.types.allowed_rendition_size.AllowedRenditionSize"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAllowedRenditionSize) -> list:
    import aws_sdk_mediaconvert.types.allowed_rendition_size

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.allowed_rendition_size.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAllowedRenditionSize:
    import aws_sdk_mediaconvert.types.allowed_rendition_size

    out: __listOfAllowedRenditionSize = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.allowed_rendition_size.deserialize_json(item)
        )
    return out
