"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Hdr10Plus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max4000


class Hdr10Plus(TypedDict, closed=True):
    mastering_monitor_nits: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max4000.__integerMin0Max4000"
    ]
    """Specify the HDR10+ mastering display normalized peak luminance, in nits. This is the normalized actual peak luminance of the mastering display, as defined by ST 2094-40."""
    target_monitor_nits: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max4000.__integerMin0Max4000"
    ]
    """Specify the HDR10+ target display nominal peak luminance, in nits. This is the nominal maximum luminance of the target display as defined by ST 2094-40."""


# --- restJson1 ser/de ---
def serialize_json(value: Hdr10Plus) -> dict:
    out: dict = {}
    if "mastering_monitor_nits" in value:
        out["masteringMonitorNits"] = value["mastering_monitor_nits"]
    if "target_monitor_nits" in value:
        out["targetMonitorNits"] = value["target_monitor_nits"]
    return out


def deserialize_json(data: dict) -> Hdr10Plus:
    out: Hdr10Plus = {}  # type: ignore[typeddict-item]
    if "masteringMonitorNits" in data:
        out["mastering_monitor_nits"] = data["masteringMonitorNits"]
    if "targetMonitorNits" in data:
        out["target_monitor_nits"] = data["targetMonitorNits"]
    return out
