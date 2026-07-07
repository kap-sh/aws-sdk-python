"""Generated from Smithy shape ``com.amazonaws.medialive#StartTimecode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StartTimecode(TypedDict, closed=True):
    timecode: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF."""


# --- restJson1 ser/de ---
def serialize_json(value: StartTimecode) -> dict:
    out: dict = {}
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    return out


def deserialize_json(data: dict) -> StartTimecode:
    out: StartTimecode = {}  # type: ignore[typeddict-item]
    if "timecode" in data:
        out["timecode"] = data["timecode"]
    return out
