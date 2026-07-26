"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateSnapshotRequest``."""

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError


class UpdateSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "str"
    """<p>The name of the snapshot.</p>"""
    retention_period: NotRequired["int"]
    """<p>The new retention period of the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotRequest) -> dict:
    out: dict = {}
    out["snapshotName"] = value["snapshot_name"]
    if "retention_period" in value:
        out["retentionPeriod"] = value["retention_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotRequest:
    out: UpdateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("UpdateSnapshotRequest.snapshot_name required")
    if "retentionPeriod" in data:
        out["retention_period"] = data["retentionPeriod"]
    return out
