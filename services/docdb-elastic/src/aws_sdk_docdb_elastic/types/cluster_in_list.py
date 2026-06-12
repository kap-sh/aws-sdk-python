"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterInList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.status


class ClusterInList(TypedDict):
    cluster_name: "str"
    """<p>The name of the elastic cluster.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "aws_sdk_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInList) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ClusterInList:
    out: ClusterInList = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("ClusterInList.cluster_name required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("ClusterInList.cluster_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ClusterInList.status required")
    return out
