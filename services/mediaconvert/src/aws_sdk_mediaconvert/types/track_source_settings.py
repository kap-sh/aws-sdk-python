"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TrackSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647


class TrackSourceSettings(TypedDict, closed=True):
    stream_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Use this setting to select a single captions track from a source. Stream numbers include all tracks in the source file, regardless of type, and correspond to either the order of tracks in the file, or if applicable, the stream number metadata of the track. Although all tracks count toward these stream numbers, in this caption selector context, only the stream number of a track containing caption data may be used. To include more than one captions track in your job outputs, create multiple input captions selectors. Specify one stream per selector. If your source file contains a track which is not recognized by the service, then the corresponding stream number will still be reserved for future use. If more types of caption data get recognized in the future, these numberings will not shift."""
    track_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Use this setting to select a single captions track from a source. Track numbers correspond to the order in the captions source file. For IMF sources, track numbering is based on the order that the captions appear in the CPL. For example, use 1 to select the captions asset that is listed first in the CPL. To include more than one captions track in your job outputs, create multiple input captions selectors. Specify one track per selector. If more types of caption data get recognized in the future, these numberings may shift, but the numberings used for streamNumber will not."""


# --- restJson1 ser/de ---
def serialize_json(value: TrackSourceSettings) -> dict:
    out: dict = {}
    if "stream_number" in value:
        out["streamNumber"] = value["stream_number"]
    if "track_number" in value:
        out["trackNumber"] = value["track_number"]
    return out


def deserialize_json(data: dict) -> TrackSourceSettings:
    out: TrackSourceSettings = {}  # type: ignore[typeddict-item]
    if "streamNumber" in data:
        out["stream_number"] = data["streamNumber"]
    if "trackNumber" in data:
        out["track_number"] = data["trackNumber"]
    return out
