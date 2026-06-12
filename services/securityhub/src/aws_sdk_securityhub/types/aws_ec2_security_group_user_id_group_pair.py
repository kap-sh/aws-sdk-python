"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupUserIdGroupPair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SecurityGroupUserIdGroupPair(TypedDict):
    group_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the security group.</p>"""
    peering_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of a VPC peering connection, if applicable.</p>"""
    user_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of an Amazon Web Services account.</p> <p>For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.</p> <p>[EC2-Classic] Required when adding or removing rules that reference a security group in another VPC. </p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the VPC for the referenced security group, if applicable.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the VPC peering connection, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupUserIdGroupPair) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "peering_status" in value:
        out["PeeringStatus"] = value["peering_status"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupUserIdGroupPair:
    out: AwsEc2SecurityGroupUserIdGroupPair = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "PeeringStatus" in data:
        out["peering_status"] = data["PeeringStatus"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    return out
