"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfForceIncludeRenditionSize``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.force_include_rendition_size

__listOfForceIncludeRenditionSize: TypeAlias = list[
    "aws_sdk_mediaconvert.types.force_include_rendition_size.ForceIncludeRenditionSize"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfForceIncludeRenditionSize) -> list:
    import aws_sdk_mediaconvert.types.force_include_rendition_size

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.force_include_rendition_size.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfForceIncludeRenditionSize:
    import aws_sdk_mediaconvert.types.force_include_rendition_size

    out: __listOfForceIncludeRenditionSize = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.force_include_rendition_size.deserialize_json(
                item
            )
        )
    return out
