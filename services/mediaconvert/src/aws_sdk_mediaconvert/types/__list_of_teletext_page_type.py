"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfTeletextPageType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.teletext_page_type

__listOfTeletextPageType: TypeAlias = list[
    "aws_sdk_mediaconvert.types.teletext_page_type.TeletextPageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTeletextPageType) -> list:
    import aws_sdk_mediaconvert.types.teletext_page_type

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.teletext_page_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTeletextPageType:
    import aws_sdk_mediaconvert.types.teletext_page_type

    out: __listOfTeletextPageType = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.teletext_page_type.deserialize_json(item))
    return out
