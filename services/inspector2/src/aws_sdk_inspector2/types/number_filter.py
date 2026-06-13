"""Generated from Smithy shape ``com.amazonaws.inspector2#NumberFilter``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NumberFilter(TypedDict):
    upper_inclusive: NotRequired["float"]
    """<p>The highest number to be included in the filter.</p>"""
    lower_inclusive: NotRequired["float"]
    """<p>The lowest number to be included in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilter) -> dict:
    out: dict = {}
    if "upper_inclusive" in value:
        out["upperInclusive"] = value["upper_inclusive"]
    if "lower_inclusive" in value:
        out["lowerInclusive"] = value["lower_inclusive"]
    return out


def deserialize_json(data: dict) -> NumberFilter:
    out: NumberFilter = {}  # type: ignore[typeddict-item]
    if "upperInclusive" in data:
        out["upper_inclusive"] = data["upperInclusive"]
    if "lowerInclusive" in data:
        out["lower_inclusive"] = data["lowerInclusive"]
    return out
