"""Generated from Smithy shape ``com.amazonaws.mgn#ImportTaskSummaryWaves``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.positive_integer


class ImportTaskSummaryWaves(TypedDict, closed=True):
    created_count: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Import task summery waves created count.</p>"""
    modified_count: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Import task summery waves modified count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskSummaryWaves) -> dict:
    out: dict = {}
    out["createdCount"] = value.get("created_count", 0)
    out["modifiedCount"] = value.get("modified_count", 0)
    return out


def deserialize_json(data: dict) -> ImportTaskSummaryWaves:
    out: ImportTaskSummaryWaves = {}  # type: ignore[typeddict-item]
    if "createdCount" in data:
        out["created_count"] = data["createdCount"]
    else:
        out["created_count"] = 0
    if "modifiedCount" in data:
        out["modified_count"] = data["modifiedCount"]
    else:
        out["modified_count"] = 0
    return out
