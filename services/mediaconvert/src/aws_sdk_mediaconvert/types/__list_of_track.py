"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfTrack``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.track

__listOfTrack: TypeAlias = list["aws_sdk_mediaconvert.types.track.Track"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTrack) -> list:
    import aws_sdk_mediaconvert.types.track

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.track.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTrack:
    import aws_sdk_mediaconvert.types.track

    out: __listOfTrack = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.track.deserialize_json(item))
    return out
