"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceVpcSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbInstanceVpcSecurityGroup(TypedDict, closed=True):
    vpc_security_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the VPC security group.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the VPC security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceVpcSecurityGroup) -> dict:
    out: dict = {}
    if "vpc_security_group_id" in value:
        out["VpcSecurityGroupId"] = value["vpc_security_group_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbInstanceVpcSecurityGroup:
    out: AwsRdsDbInstanceVpcSecurityGroup = {}  # type: ignore[typeddict-item]
    if "VpcSecurityGroupId" in data:
        out["vpc_security_group_id"] = data["VpcSecurityGroupId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
