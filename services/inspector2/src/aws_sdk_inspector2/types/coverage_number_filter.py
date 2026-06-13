"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageNumberFilter``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CoverageNumberFilter(TypedDict):
    upper_inclusive: NotRequired["int"]
    """<p>The upper inclusive for the coverage number.&gt;</p>"""
    lower_inclusive: NotRequired["int"]
    """<p>The lower inclusive for the coverage number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageNumberFilter) -> dict:
    out: dict = {}
    if "upper_inclusive" in value:
        out["upperInclusive"] = value["upper_inclusive"]
    if "lower_inclusive" in value:
        out["lowerInclusive"] = value["lower_inclusive"]
    return out


def deserialize_json(data: dict) -> CoverageNumberFilter:
    out: CoverageNumberFilter = {}  # type: ignore[typeddict-item]
    if "upperInclusive" in data:
        out["upper_inclusive"] = data["upperInclusive"]
    if "lowerInclusive" in data:
        out["lower_inclusive"] = data["lowerInclusive"]
    return out
