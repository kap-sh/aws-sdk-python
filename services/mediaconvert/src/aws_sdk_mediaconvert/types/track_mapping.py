"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TrackMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__integer


class TrackMapping(TypedDict, closed=True):
    audio_track_indexes: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer.__listOf__integer"
    ]
    """The index numbers of the audio tracks in your media file."""
    data_track_indexes: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer.__listOf__integer"
    ]
    """The index numbers of the data tracks in your media file."""
    video_track_indexes: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer.__listOf__integer"
    ]
    """The index numbers of the video tracks in your media file."""


# --- restJson1 ser/de ---
def serialize_json(value: TrackMapping) -> dict:
    out: dict = {}
    if "audio_track_indexes" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["audioTrackIndexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.serialize_json(
                value["audio_track_indexes"]
            )
        )
    if "data_track_indexes" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["dataTrackIndexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.serialize_json(
                value["data_track_indexes"]
            )
        )
    if "video_track_indexes" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["videoTrackIndexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.serialize_json(
                value["video_track_indexes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrackMapping:
    out: TrackMapping = {}  # type: ignore[typeddict-item]
    if "audioTrackIndexes" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["audio_track_indexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.deserialize_json(
                data["audioTrackIndexes"]
            )
        )
    if "dataTrackIndexes" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["data_track_indexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.deserialize_json(
                data["dataTrackIndexes"]
            )
        )
    if "videoTrackIndexes" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer

        out["video_track_indexes"] = (
            aws_sdk_mediaconvert.types.__list_of__integer.deserialize_json(
                data["videoTrackIndexes"]
            )
        )
    return out
