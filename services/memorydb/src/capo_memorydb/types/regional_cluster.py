"""Generated from Smithy shape ``com.amazonaws.memorydb#RegionalCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class RegionalCluster(TypedDict, closed=True):
    cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the Regional cluster</p>"""
    region: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Region the current Regional cluster is assigned to.</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the Regional cluster.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) the Regional cluster</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionalCluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "region" in value:
        out["Region"] = value["region"]
    if "status" in value:
        out["Status"] = value["status"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionalCluster:
    out: RegionalCluster = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
