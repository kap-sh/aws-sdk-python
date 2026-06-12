"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__mapOfCaptionSelector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.caption_selector

__mapOfCaptionSelector: TypeAlias = dict[
    "aws_sdk_mediaconvert.types.__string.__string",
    "aws_sdk_mediaconvert.types.caption_selector.CaptionSelector",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOfCaptionSelector) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mediaconvert.types.caption_selector

        out[key] = aws_sdk_mediaconvert.types.caption_selector.serialize_json(value)
    return out


def deserialize_json(data: dict) -> __mapOfCaptionSelector:
    out: __mapOfCaptionSelector = {}
    for key, value in data.items():
        import aws_sdk_mediaconvert.types.caption_selector

        out[key] = aws_sdk_mediaconvert.types.caption_selector.deserialize_json(value)
    return out
