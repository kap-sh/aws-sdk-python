"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisResultSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.subnet_id
    import aws_sdk_mgn.types.vpc_id


class NetworkMigrationAnalysisResultSource(TypedDict, closed=True):
    vpc_id: NotRequired["aws_sdk_mgn.types.vpc_id.VpcID"]
    """<p>The VPC ID of the source resource.</p>"""
    subnet_id: NotRequired["aws_sdk_mgn.types.subnet_id.SubnetID"]
    """<p>The subnet ID of the source resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysisResultSource) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcID"] = value["vpc_id"]
    if "subnet_id" in value:
        out["subnetID"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationAnalysisResultSource:
    out: NetworkMigrationAnalysisResultSource = {}  # type: ignore[typeddict-item]
    if "vpcID" in data:
        out["vpc_id"] = data["vpcID"]
    if "subnetID" in data:
        out["subnet_id"] = data["subnetID"]
    return out
