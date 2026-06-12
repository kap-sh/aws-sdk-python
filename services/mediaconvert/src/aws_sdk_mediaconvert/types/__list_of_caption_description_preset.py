"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfCaptionDescriptionPreset``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.caption_description_preset

__listOfCaptionDescriptionPreset: TypeAlias = list[
    "aws_sdk_mediaconvert.types.caption_description_preset.CaptionDescriptionPreset"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCaptionDescriptionPreset) -> list:
    import aws_sdk_mediaconvert.types.caption_description_preset

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.caption_description_preset.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCaptionDescriptionPreset:
    import aws_sdk_mediaconvert.types.caption_description_preset

    out: __listOfCaptionDescriptionPreset = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.caption_description_preset.deserialize_json(item)
        )
    return out
