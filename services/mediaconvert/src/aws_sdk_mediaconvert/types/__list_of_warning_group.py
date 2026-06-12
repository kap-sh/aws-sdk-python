"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfWarningGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.warning_group

__listOfWarningGroup: TypeAlias = list[
    "aws_sdk_mediaconvert.types.warning_group.WarningGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfWarningGroup) -> list:
    import aws_sdk_mediaconvert.types.warning_group

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.warning_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfWarningGroup:
    import aws_sdk_mediaconvert.types.warning_group

    out: __listOfWarningGroup = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.warning_group.deserialize_json(item))
    return out
