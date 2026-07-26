"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.integer


class DataSetImportSummary(TypedDict, closed=True):
    total: "capo_m2.types.integer.Integer"
    """<p>The total number of data set imports.</p>"""
    succeeded: "capo_m2.types.integer.Integer"
    """<p>The number of data set imports that have succeeded.</p>"""
    failed: "capo_m2.types.integer.Integer"
    """<p>The number of data set imports that have failed.</p>"""
    pending: "capo_m2.types.integer.Integer"
    """<p>The number of data set imports that are pending.</p>"""
    in_progress: "capo_m2.types.integer.Integer"
    """<p>The number of data set imports that are in progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportSummary) -> dict:
    out: dict = {}
    out["total"] = value.get("total", 0)
    out["succeeded"] = value.get("succeeded", 0)
    out["failed"] = value.get("failed", 0)
    out["pending"] = value.get("pending", 0)
    out["inProgress"] = value.get("in_progress", 0)
    return out


def deserialize_json(data: dict) -> DataSetImportSummary:
    out: DataSetImportSummary = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    if "succeeded" in data:
        out["succeeded"] = data["succeeded"]
    else:
        out["succeeded"] = 0
    if "failed" in data:
        out["failed"] = data["failed"]
    else:
        out["failed"] = 0
    if "pending" in data:
        out["pending"] = data["pending"]
    else:
        out["pending"] = 0
    if "inProgress" in data:
        out["in_progress"] = data["inProgress"]
    else:
        out["in_progress"] = 0
    return out
