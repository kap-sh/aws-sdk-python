"""Generated from Smithy shape ``com.amazonaws.mgn#ImportTaskSummaryServers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.positive_integer


class ImportTaskSummaryServers(TypedDict, closed=True):
    created_count: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Import task summary servers created count.</p>"""
    modified_count: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Import task summary servers modified count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskSummaryServers) -> dict:
    out: dict = {}
    out["createdCount"] = value.get("created_count", 0)
    out["modifiedCount"] = value.get("modified_count", 0)
    return out


def deserialize_json(data: dict) -> ImportTaskSummaryServers:
    out: ImportTaskSummaryServers = {}  # type: ignore[typeddict-item]
    if "createdCount" in data:
        out["created_count"] = data["createdCount"]
    else:
        out["created_count"] = 0
    if "modifiedCount" in data:
        out["modified_count"] = data["modifiedCount"]
    else:
        out["modified_count"] = 0
    return out
