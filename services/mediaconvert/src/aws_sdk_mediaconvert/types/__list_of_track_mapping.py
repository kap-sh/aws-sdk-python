"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfTrackMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.track_mapping

__listOfTrackMapping: TypeAlias = list[
    "aws_sdk_mediaconvert.types.track_mapping.TrackMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTrackMapping) -> list:
    import aws_sdk_mediaconvert.types.track_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.track_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTrackMapping:
    import aws_sdk_mediaconvert.types.track_mapping

    out: __listOfTrackMapping = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.track_mapping.deserialize_json(item))
    return out
