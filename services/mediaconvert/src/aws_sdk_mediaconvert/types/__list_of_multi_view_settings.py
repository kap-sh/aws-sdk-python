"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfMultiViewSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.multi_view_settings

__listOfMultiViewSettings: TypeAlias = list[
    "aws_sdk_mediaconvert.types.multi_view_settings.MultiViewSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiViewSettings) -> list:
    import aws_sdk_mediaconvert.types.multi_view_settings

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.multi_view_settings.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMultiViewSettings:
    import aws_sdk_mediaconvert.types.multi_view_settings

    out: __listOfMultiViewSettings = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.multi_view_settings.deserialize_json(item)
        )
    return out
