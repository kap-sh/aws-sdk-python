"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SecurityGroupDetails(TypedDict):
    group_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the security group.</p>"""
    group_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the security group.</p>"""
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account ID of the owner of the security group.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>[VPC only] The ID of the VPC for the security group.</p>"""
    ip_permissions: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.AwsEc2SecurityGroupIpPermissionList"
    ]
    """<p>The inbound rules associated with the security group.</p>"""
    ip_permissions_egress: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.AwsEc2SecurityGroupIpPermissionList"
    ]
    """<p>[VPC only] The outbound rules associated with the security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupDetails) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "ip_permissions" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list

        out["IpPermissions"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.serialize_json(
                value["ip_permissions"]
            )
        )
    if "ip_permissions_egress" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list

        out["IpPermissionsEgress"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.serialize_json(
                value["ip_permissions_egress"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupDetails:
    out: AwsEc2SecurityGroupDetails = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "IpPermissions" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list

        out["ip_permissions"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.deserialize_json(
                data["IpPermissions"]
            )
        )
    if "IpPermissionsEgress" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list

        out["ip_permissions_egress"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_permission_list.deserialize_json(
                data["IpPermissionsEgress"]
            )
        )
    return out
