"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisResultTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.subnet_id
    import aws_sdk_mgn.types.vpc_id


class NetworkMigrationAnalysisResultTarget(TypedDict):
    vpc_id: NotRequired["aws_sdk_mgn.types.vpc_id.VpcID"]
    """<p>The VPC ID of the target resource.</p>"""
    subnet_id: NotRequired["aws_sdk_mgn.types.subnet_id.SubnetID"]
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
