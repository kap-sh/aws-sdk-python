"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessResourceTypeDetails``."""

from typing_extensions import NotRequired, TypedDict


class InternalAccessResourceTypeDetails(TypedDict, closed=True):
    total_active_findings: NotRequired["int"]
    """<p>The total number of active findings for the resource type in the internal access analyzer.</p>"""
    total_resolved_findings: NotRequired["int"]
    """<p>The total number of resolved findings for the resource type in the internal access analyzer.</p>"""
    total_archived_findings: NotRequired["int"]
    """<p>The total number of archived findings for the resource type in the internal access analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessResourceTypeDetails) -> dict:
    out: dict = {}
    if "total_active_findings" in value:
        out["totalActiveFindings"] = value["total_active_findings"]
    if "total_resolved_findings" in value:
        out["totalResolvedFindings"] = value["total_resolved_findings"]
    if "total_archived_findings" in value:
        out["totalArchivedFindings"] = value["total_archived_findings"]
    return out


def deserialize_json(data: dict) -> InternalAccessResourceTypeDetails:
    out: InternalAccessResourceTypeDetails = {}  # type: ignore[typeddict-item]
    if "totalActiveFindings" in data:
        out["total_active_findings"] = data["totalActiveFindings"]
    if "totalResolvedFindings" in data:
        out["total_resolved_findings"] = data["totalResolvedFindings"]
    if "totalArchivedFindings" in data:
        out["total_archived_findings"] = data["totalArchivedFindings"]
    return out
