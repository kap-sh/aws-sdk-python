"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisResultTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.subnet_id
    import capo_mgn.types.vpc_id


class NetworkMigrationAnalysisResultTarget(TypedDict, closed=True):
    vpc_id: NotRequired["capo_mgn.types.vpc_id.VpcID"]
    """<p>The VPC ID of the target resource.</p>"""
    subnet_id: NotRequired["capo_mgn.types.subnet_id.SubnetID"]
    """<p>The subnet ID of the target resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysisResultTarget) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcID"] = value["vpc_id"]
    if "subnet_id" in value:
        out["subnetID"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationAnalysisResultTarget:
    out: NetworkMigrationAnalysisResultTarget = {}  # type: ignore[typeddict-item]
    if "vpcID" in data:
        out["vpc_id"] = data["vpcID"]
    if "subnetID" in data:
        out["subnet_id"] = data["subnetID"]
    return out
