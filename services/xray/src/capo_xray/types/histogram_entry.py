"""Generated from Smithy shape ``com.amazonaws.xray#HistogramEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.double
    import capo_xray.types.integer


class HistogramEntry(TypedDict, closed=True):
    value: "capo_xray.types.double.Double"
    """<p>The value of the entry.</p>"""
    count: "capo_xray.types.integer.Integer"
    """<p>The prevalence of the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramEntry) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    out["Count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> HistogramEntry:
    out: HistogramEntry = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
