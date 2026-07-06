"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#VpcSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.vpc_security_group_id


class VpcSecurityGroupMembership(TypedDict, closed=True):
    vpc_security_group_id: NotRequired[
        "aws_sdk_redshift_serverless.types.vpc_security_group_id.VpcSecurityGroupId"
    ]
    """<p>The unique identifier of the VPC security group.</p>"""
    status: NotRequired["str"]
    """<p>The status of the VPC security group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSecurityGroupMembership) -> dict:
    out: dict = {}
    if "vpc_security_group_id" in value:
        out["vpcSecurityGroupId"] = value["vpc_security_group_id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcSecurityGroupMembership:
    out: VpcSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if "vpcSecurityGroupId" in data:
        out["vpc_security_group_id"] = data["vpcSecurityGroupId"]
    if "status" in data:
        out["status"] = data["status"]
    return out
