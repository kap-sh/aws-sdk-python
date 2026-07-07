"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteSnapshotRequest``."""

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError


class DeleteSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "str"
    """<p>The name of the snapshot to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    out["snapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("DeleteSnapshotRequest.snapshot_name required")
    return out
