"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNoticeDetailRange``."""

from typing_extensions import NotRequired, TypedDict


class RouteNoticeDetailRange(TypedDict, closed=True):
    min: NotRequired["int"]
    """<p>Minimum value for the range.</p>"""
    max: NotRequired["int"]
    """<p>Maximum value for the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteNoticeDetailRange) -> dict:
    out: dict = {}
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    return out


def deserialize_json(data: dict) -> RouteNoticeDetailRange:
    out: RouteNoticeDetailRange = {}  # type: ignore[typeddict-item]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    return out
