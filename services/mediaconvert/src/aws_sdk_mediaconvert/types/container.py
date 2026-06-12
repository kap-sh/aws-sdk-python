"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Container``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double
    import aws_sdk_mediaconvert.types.__list_of_track
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.format


class Container(TypedDict):
    duration: NotRequired["aws_sdk_mediaconvert.types.__double.__double"]
    """The total duration of your media file, in seconds."""
    format: NotRequired["aws_sdk_mediaconvert.types.format.Format"]
    """The format of your media file. For example: MP4, QuickTime (MOV), Matroska (MKV), WebM, MXF, Wave, AVI, MPEG-TS, or MPEG-PS. Note that this will be blank if your media file has a format that the MediaConvert Probe operation does not recognize."""
    start_timecode: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The start timecode of the media file, in HH:MM:SS:FF format (or HH:MM:SS;FF for drop frame timecode). Note that this field is null when the container does not include an embedded start timecode."""
    tracks: NotRequired["aws_sdk_mediaconvert.types.__list_of_track.__listOfTrack"]
    """Details about each track (video, audio, or data) in the media file."""


# --- restJson1 ser/de ---
def serialize_json(value: Container) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "format" in value:
        import aws_sdk_mediaconvert.types.format

        out["format"] = aws_sdk_mediaconvert.types.format.serialize_json(
            value["format"]
        )
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    if "tracks" in value:
        import aws_sdk_mediaconvert.types.__list_of_track

        out["tracks"] = aws_sdk_mediaconvert.types.__list_of_track.serialize_json(
            value["tracks"]
        )
    return out


def deserialize_json(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "format" in data:
        import aws_sdk_mediaconvert.types.format

        out["format"] = aws_sdk_mediaconvert.types.format.deserialize_json(
            data["format"]
        )
    if "startTimecode" in data:
        out["start_timecode"] = data["startTimecode"]
    if "tracks" in data:
        import aws_sdk_mediaconvert.types.__list_of_track

        out["tracks"] = aws_sdk_mediaconvert.types.__list_of_track.deserialize_json(
            data["tracks"]
        )
    return out
