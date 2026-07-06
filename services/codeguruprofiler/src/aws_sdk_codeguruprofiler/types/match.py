"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Match``."""

from typing_extensions import NotRequired, TypedDict


class Match(TypedDict, closed=True):
    target_frames_index: NotRequired["int"]
    """<p>The target frame that triggered a match.</p>"""
    frame_address: NotRequired["str"]
    """<p>The location in the profiling graph that contains a recommendation found during analysis.</p>"""
    threshold_breach_value: NotRequired["float"]
    """<p>The value in the profile data that exceeded the recommendation threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Match) -> dict:
    out: dict = {}
    if "target_frames_index" in value:
        out["targetFramesIndex"] = value["target_frames_index"]
    if "frame_address" in value:
        out["frameAddress"] = value["frame_address"]
    if "threshold_breach_value" in value:
        out["thresholdBreachValue"] = value["threshold_breach_value"]
    return out


def deserialize_json(data: dict) -> Match:
    out: Match = {}  # type: ignore[typeddict-item]
    if "targetFramesIndex" in data:
        out["target_frames_index"] = data["targetFramesIndex"]
    if "frameAddress" in data:
        out["frame_address"] = data["frameAddress"]
    if "thresholdBreachValue" in data:
        out["threshold_breach_value"] = data["thresholdBreachValue"]
    return out
