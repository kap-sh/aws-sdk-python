"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfVideoDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.video_description

__listOfVideoDescription: TypeAlias = list[
    "aws_sdk_medialive.types.video_description.VideoDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoDescription) -> list:
    import aws_sdk_medialive.types.video_description

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.video_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVideoDescription:
    import aws_sdk_medialive.types.video_description

    out: __listOfVideoDescription = []
    for item in data:
        out.append(aws_sdk_medialive.types.video_description.deserialize_json(item))
    return out
