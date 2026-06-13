"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchScopeSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SearchScopeSummary(TypedDict):
    total_recovery_points_to_scan_count: NotRequired["int"]
    """<p>This is the count of the total number of backups that will be scanned in a search.</p>"""
    total_items_to_scan_count: NotRequired["int"]
    """<p>This is the count of the total number of items that will be scanned in a search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchScopeSummary) -> dict:
    out: dict = {}
    if "total_recovery_points_to_scan_count" in value:
        out["TotalRecoveryPointsToScanCount"] = value[
            "total_recovery_points_to_scan_count"
        ]
    if "total_items_to_scan_count" in value:
        out["TotalItemsToScanCount"] = value["total_items_to_scan_count"]
    return out


def deserialize_json(data: dict) -> SearchScopeSummary:
    out: SearchScopeSummary = {}  # type: ignore[typeddict-item]
    if "TotalRecoveryPointsToScanCount" in data:
        out["total_recovery_points_to_scan_count"] = data[
            "TotalRecoveryPointsToScanCount"
        ]
    if "TotalItemsToScanCount" in data:
        out["total_items_to_scan_count"] = data["TotalItemsToScanCount"]
    return out
