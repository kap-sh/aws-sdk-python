"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Id3Insertion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern010920405090509092
    import aws_sdk_mediaconvert.types.__string_pattern_a_za_z0902


class Id3Insertion(TypedDict):
    id3: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_a_za_z0902.__stringPatternAZaZ0902"
    ]
    """Use ID3 tag to provide a fully formed ID3 tag in base64-encode format."""
    timecode: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Provide a Timecode in HH:MM:SS:FF or HH:MM:SS;FF format."""


# --- restJson1 ser/de ---
def serialize_json(value: Id3Insertion) -> dict:
    out: dict = {}
    if "id3" in value:
        out["id3"] = value["id3"]
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    return out


def deserialize_json(data: dict) -> Id3Insertion:
    out: Id3Insertion = {}  # type: ignore[typeddict-item]
    if "id3" in data:
        out["id3"] = data["id3"]
    if "timecode" in data:
        out["timecode"] = data["timecode"]
    return out
