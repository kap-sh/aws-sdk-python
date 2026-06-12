"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterVpcSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterVpcSecurityGroup(TypedDict):
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the VPC security group.</p>"""
    vpc_security_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the VPC security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterVpcSecurityGroup) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "vpc_security_group_id" in value:
        out["VpcSecurityGroupId"] = value["vpc_security_group_id"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterVpcSecurityGroup:
    out: AwsRedshiftClusterVpcSecurityGroup = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "VpcSecurityGroupId" in data:
        out["vpc_security_group_id"] = data["VpcSecurityGroupId"]
    return out
