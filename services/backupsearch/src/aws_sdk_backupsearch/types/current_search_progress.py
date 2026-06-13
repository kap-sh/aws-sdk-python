"""Generated from Smithy shape ``com.amazonaws.backupsearch#CurrentSearchProgress``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CurrentSearchProgress(TypedDict):
    recovery_points_scanned_count: NotRequired["int"]
    """<p>This number is the sum of all backups that have been scanned so far during a search job.</p>"""
    items_scanned_count: NotRequired["int"]
    """<p>This number is the sum of all items that have been scanned so far during a search job.</p>"""
    items_matched_count: NotRequired["int"]
    """<p>This number is the sum of all items that match the item filters in a search job in progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentSearchProgress) -> dict:
    out: dict = {}
    if "recovery_points_scanned_count" in value:
        out["RecoveryPointsScannedCount"] = value["recovery_points_scanned_count"]
    if "items_scanned_count" in value:
        out["ItemsScannedCount"] = value["items_scanned_count"]
    if "items_matched_count" in value:
        out["ItemsMatchedCount"] = value["items_matched_count"]
    return out


def deserialize_json(data: dict) -> CurrentSearchProgress:
    out: CurrentSearchProgress = {}  # type: ignore[typeddict-item]
    if "RecoveryPointsScannedCount" in data:
        out["recovery_points_scanned_count"] = data["RecoveryPointsScannedCount"]
    if "ItemsScannedCount" in data:
        out["items_scanned_count"] = data["ItemsScannedCount"]
    if "ItemsMatchedCount" in data:
        out["items_matched_count"] = data["ItemsMatchedCount"]
    return out
