"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfTrackMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.track_mapping

__listOfTrackMapping: TypeAlias = list[
    "capo_mediaconvert.types.track_mapping.TrackMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTrackMapping) -> list:
    import capo_mediaconvert.types.track_mapping

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.track_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTrackMapping:
    import capo_mediaconvert.types.track_mapping

    out: __listOfTrackMapping = []
    for item in data:
        out.append(capo_mediaconvert.types.track_mapping.deserialize_json(item))
    return out
