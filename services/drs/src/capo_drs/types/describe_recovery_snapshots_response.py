"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoverySnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_snapshots_list


class DescribeRecoverySnapshotsResponse(TypedDict, closed=True):
    items: NotRequired["capo_drs.types.recovery_snapshots_list.RecoverySnapshotsList"]
    """<p>An array of Recovery Snapshots.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Snapshot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoverySnapshotsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_drs.types.recovery_snapshots_list

        out["items"] = capo_drs.types.recovery_snapshots_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeRecoverySnapshotsResponse:
    out: DescribeRecoverySnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_drs.types.recovery_snapshots_list

        out["items"] = capo_drs.types.recovery_snapshots_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
