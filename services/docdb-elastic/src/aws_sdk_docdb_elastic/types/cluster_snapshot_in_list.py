"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshotInList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.status


class ClusterSnapshotInList(TypedDict, closed=True):
    snapshot_name: "str"
    """<p>The name of the elastic cluster snapshot.</p>"""
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "aws_sdk_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster snapshot.</p>"""
    snapshot_creation_time: "str"
    """<p>The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshotInList) -> dict:
    out: dict = {}
    out["snapshotName"] = value["snapshot_name"]
    out["snapshotArn"] = value["snapshot_arn"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    out["snapshotCreationTime"] = value["snapshot_creation_time"]
    return out


def deserialize_json(data: dict) -> ClusterSnapshotInList:
    out: ClusterSnapshotInList = {}  # type: ignore[typeddict-item]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("ClusterSnapshotInList.snapshot_name required")
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    else:
        raise DeserializationError("ClusterSnapshotInList.snapshot_arn required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("ClusterSnapshotInList.cluster_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ClusterSnapshotInList.status required")
    if "snapshotCreationTime" in data:
        out["snapshot_creation_time"] = data["snapshotCreationTime"]
    else:
        raise DeserializationError(
            "ClusterSnapshotInList.snapshot_creation_time required"
        )
    return out
