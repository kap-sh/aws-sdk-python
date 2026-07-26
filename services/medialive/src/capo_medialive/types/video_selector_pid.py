"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorPid``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max8191


class VideoSelectorPid(TypedDict, closed=True):
    pid: NotRequired["capo_medialive.types.__integer_min0_max8191.__integerMin0Max8191"]
    """Selects a specific PID from within a video source."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorPid) -> dict:
    out: dict = {}
    if "pid" in value:
        out["pid"] = value["pid"]
    return out


def deserialize_json(data: dict) -> VideoSelectorPid:
    out: VideoSelectorPid = {}  # type: ignore[typeddict-item]
    if "pid" in data:
        out["pid"] = data["pid"]
    return out
