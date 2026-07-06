"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetSnapshotRequest``."""

from typing_extensions import NotRequired, TypedDict


class GetSnapshotRequest(TypedDict, closed=True):
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot to return.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services account of a snapshot shared with another user.</p>"""
    snapshot_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the snapshot to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnapshotRequest) -> dict:
    out: dict = {}
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnapshotRequest:
    out: GetSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    return out
