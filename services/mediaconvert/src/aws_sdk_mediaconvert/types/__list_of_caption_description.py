"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfCaptionDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.caption_description

__listOfCaptionDescription: TypeAlias = list[
    "aws_sdk_mediaconvert.types.caption_description.CaptionDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCaptionDescription) -> list:
    import aws_sdk_mediaconvert.types.caption_description

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.caption_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCaptionDescription:
    import aws_sdk_mediaconvert.types.caption_description

    out: __listOfCaptionDescription = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.caption_description.deserialize_json(item)
        )
    return out
