"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCaptionSelector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.caption_selector

__listOfCaptionSelector: TypeAlias = list[
    "aws_sdk_medialive.types.caption_selector.CaptionSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCaptionSelector) -> list:
    import aws_sdk_medialive.types.caption_selector

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.caption_selector.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCaptionSelector:
    import aws_sdk_medialive.types.caption_selector

    out: __listOfCaptionSelector = []
    for item in data:
        out.append(aws_sdk_medialive.types.caption_selector.deserialize_json(item))
    return out
