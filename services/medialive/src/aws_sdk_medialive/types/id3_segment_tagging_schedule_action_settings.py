"""Generated from Smithy shape ``com.amazonaws.medialive#Id3SegmentTaggingScheduleActionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class Id3SegmentTaggingScheduleActionSettings(TypedDict):
    id3: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: http://id3.org/id3v2.4.0-structure"""
    tag: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number."""


# --- restJson1 ser/de ---
def serialize_json(value: Id3SegmentTaggingScheduleActionSettings) -> dict:
    out: dict = {}
    if "id3" in value:
        out["id3"] = value["id3"]
    if "tag" in value:
        out["tag"] = value["tag"]
    return out


def deserialize_json(data: dict) -> Id3SegmentTaggingScheduleActionSettings:
    out: Id3SegmentTaggingScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "id3" in data:
        out["id3"] = data["id3"]
    if "tag" in data:
        out["tag"] = data["tag"]
    return out
