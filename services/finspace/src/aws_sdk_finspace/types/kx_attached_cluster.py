"""Generated from Smithy shape ``com.amazonaws.finspace#KxAttachedCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_cluster_status
    import aws_sdk_finspace.types.kx_cluster_type


class KxAttachedCluster(TypedDict, closed=True):
    cluster_name: NotRequired["aws_sdk_finspace.types.kx_cluster_name.KxClusterName"]
    """<p>A unique name for the attached cluster.</p>"""
    cluster_type: NotRequired["aws_sdk_finspace.types.kx_cluster_type.KxClusterType"]
    """<p>Specifies the type of cluster. The volume for TP and RDB cluster types will be used for TP logs.</p>"""
    cluster_status: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_status.KxClusterStatus"
    ]
    """<p>The status of the attached cluster.</p> <ul> <li> <p>PENDING – The cluster is pending creation.</p> </li> <li> <p>CREATING – The cluster creation process is in progress.</p> </li> <li> <p>CREATE_FAILED – The cluster creation process has failed.</p> </li> <li> <p>RUNNING – The cluster creation process is running.</p> </li> <li> <p>UPDATING – The cluster is in the process of being updated.</p> </li> <li> <p>DELETING – The cluster is in the process of being deleted.</p> </li> <li> <p>DELETED – The cluster has been deleted.</p> </li> <li> <p>DELETE_FAILED – The cluster failed to delete.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxAttachedCluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "cluster_type" in value:
        import aws_sdk_finspace.types.kx_cluster_type

        out["clusterType"] = aws_sdk_finspace.types.kx_cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "cluster_status" in value:
        import aws_sdk_finspace.types.kx_cluster_status

        out["clusterStatus"] = aws_sdk_finspace.types.kx_cluster_status.serialize_json(
            value["cluster_status"]
        )
    return out


def deserialize_json(data: dict) -> KxAttachedCluster:
    out: KxAttachedCluster = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "clusterType" in data:
        import aws_sdk_finspace.types.kx_cluster_type

        out["cluster_type"] = aws_sdk_finspace.types.kx_cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "clusterStatus" in data:
        import aws_sdk_finspace.types.kx_cluster_status

        out["cluster_status"] = (
            aws_sdk_finspace.types.kx_cluster_status.deserialize_json(
                data["clusterStatus"]
            )
        )
    return out
