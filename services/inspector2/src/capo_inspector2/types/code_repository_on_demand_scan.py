"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryOnDemandScan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.commit_id
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.scan_status


class CodeRepositoryOnDemandScan(TypedDict, closed=True):
    last_scanned_commit_id: NotRequired["capo_inspector2.types.commit_id.CommitId"]
    """<p>The ID of the last commit that was scanned during an on-demand scan.</p>"""
    last_scan_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when the last on-demand scan was performed.</p>"""
    scan_status: NotRequired["capo_inspector2.types.scan_status.ScanStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryOnDemandScan) -> dict:
    out: dict = {}
    if "last_scanned_commit_id" in value:
        out["lastScannedCommitId"] = value["last_scanned_commit_id"]
    if "last_scan_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastScanAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_scan_at"]
        )
    if "scan_status" in value:
        import capo_inspector2.types.scan_status

        out["scanStatus"] = capo_inspector2.types.scan_status.serialize_json(
            value["scan_status"]
        )
    return out


def deserialize_json(data: dict) -> CodeRepositoryOnDemandScan:
    out: CodeRepositoryOnDemandScan = {}  # type: ignore[typeddict-item]
    if "lastScannedCommitId" in data:
        out["last_scanned_commit_id"] = data["lastScannedCommitId"]
    if "lastScanAt" in data:
        import capo_inspector2.types.date_time_timestamp

        out["last_scan_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastScanAt"]
            )
        )
    if "scanStatus" in data:
        import capo_inspector2.types.scan_status

        out["scan_status"] = capo_inspector2.types.scan_status.deserialize_json(
            data["scanStatus"]
        )
    return out
