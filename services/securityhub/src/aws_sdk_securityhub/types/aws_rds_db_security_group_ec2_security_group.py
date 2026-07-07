"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupEc2SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbSecurityGroupEc2SecurityGroup(TypedDict, closed=True):
    ec2_security_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the ID for the EC2 security group.</p>"""
    ec2_security_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the name of the EC2 security group.</p>"""
    ec2_security_group_owner_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Provides the Amazon Web Services ID of the owner of the EC2 security group.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Provides the status of the EC2 security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupEc2SecurityGroup) -> dict:
    out: dict = {}
    if "ec2_security_group_id" in value:
        out["Ec2SecurityGroupId"] = value["ec2_security_group_id"]
    if "ec2_security_group_name" in value:
        out["Ec2SecurityGroupName"] = value["ec2_security_group_name"]
    if "ec2_security_group_owner_id" in value:
        out["Ec2SecurityGroupOwnerId"] = value["ec2_security_group_owner_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSecurityGroupEc2SecurityGroup:
    out: AwsRdsDbSecurityGroupEc2SecurityGroup = {}  # type: ignore[typeddict-item]
    if "Ec2SecurityGroupId" in data:
        out["ec2_security_group_id"] = data["Ec2SecurityGroupId"]
    if "Ec2SecurityGroupName" in data:
        out["ec2_security_group_name"] = data["Ec2SecurityGroupName"]
    if "Ec2SecurityGroupOwnerId" in data:
        out["ec2_security_group_owner_id"] = data["Ec2SecurityGroupOwnerId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
