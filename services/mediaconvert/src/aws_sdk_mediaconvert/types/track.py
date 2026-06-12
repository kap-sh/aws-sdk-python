"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Track``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.audio_properties
    import aws_sdk_mediaconvert.types.codec
    import aws_sdk_mediaconvert.types.data_properties
    import aws_sdk_mediaconvert.types.track_type
    import aws_sdk_mediaconvert.types.video_properties


class Track(TypedDict):
    audio_properties: NotRequired[
        "aws_sdk_mediaconvert.types.audio_properties.AudioProperties"
    ]
    """Details about the media file's audio track."""
    codec: NotRequired["aws_sdk_mediaconvert.types.codec.Codec"]
    """The codec of the audio or video track, or caption format of the data track."""
    data_properties: NotRequired[
        "aws_sdk_mediaconvert.types.data_properties.DataProperties"
    ]
    """Details about the media file's data track."""
    duration: NotRequired["aws_sdk_mediaconvert.types.__double.__double"]
    """The duration of the track, in seconds."""
    index: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The unique index number of the track, starting at 1."""
    track_type: NotRequired["aws_sdk_mediaconvert.types.track_type.TrackType"]
    """The type of track: video, audio, or data."""
    video_properties: NotRequired[
        "aws_sdk_mediaconvert.types.video_properties.VideoProperties"
    ]
    """Details about the media file's video track."""


# --- restJson1 ser/de ---
def serialize_json(value: Track) -> dict:
    out: dict = {}
    if "audio_properties" in value:
        import aws_sdk_mediaconvert.types.audio_properties

        out["audioProperties"] = (
            aws_sdk_mediaconvert.types.audio_properties.serialize_json(
                value["audio_properties"]
            )
        )
    if "codec" in value:
        import aws_sdk_mediaconvert.types.codec

        out["codec"] = aws_sdk_mediaconvert.types.codec.serialize_json(value["codec"])
    if "data_properties" in value:
        import aws_sdk_mediaconvert.types.data_properties

        out["dataProperties"] = (
            aws_sdk_mediaconvert.types.data_properties.serialize_json(
                value["data_properties"]
            )
        )
    if "duration" in value:
        out["duration"] = value["duration"]
    if "index" in value:
        out["index"] = value["index"]
    if "track_type" in value:
        import aws_sdk_mediaconvert.types.track_type

        out["trackType"] = aws_sdk_mediaconvert.types.track_type.serialize_json(
            value["track_type"]
        )
    if "video_properties" in value:
        import aws_sdk_mediaconvert.types.video_properties

        out["videoProperties"] = (
            aws_sdk_mediaconvert.types.video_properties.serialize_json(
                value["video_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Track:
    out: Track = {}  # type: ignore[typeddict-item]
    if "audioProperties" in data:
        import aws_sdk_mediaconvert.types.audio_properties

        out["audio_properties"] = (
            aws_sdk_mediaconvert.types.audio_properties.deserialize_json(
                data["audioProperties"]
            )
        )
    if "codec" in data:
        import aws_sdk_mediaconvert.types.codec

        out["codec"] = aws_sdk_mediaconvert.types.codec.deserialize_json(data["codec"])
    if "dataProperties" in data:
        import aws_sdk_mediaconvert.types.data_properties

        out["data_properties"] = (
            aws_sdk_mediaconvert.types.data_properties.deserialize_json(
                data["dataProperties"]
            )
        )
    if "duration" in data:
        out["duration"] = data["duration"]
    if "index" in data:
        out["index"] = data["index"]
    if "trackType" in data:
        import aws_sdk_mediaconvert.types.track_type

        out["track_type"] = aws_sdk_mediaconvert.types.track_type.deserialize_json(
            data["trackType"]
        )
    if "videoProperties" in data:
        import aws_sdk_mediaconvert.types.video_properties

        out["video_properties"] = (
            aws_sdk_mediaconvert.types.video_properties.deserialize_json(
                data["videoProperties"]
            )
        )
    return out
