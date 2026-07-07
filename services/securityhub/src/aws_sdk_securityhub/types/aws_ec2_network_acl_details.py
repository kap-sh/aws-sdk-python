"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkAclDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_network_acl_association_list
    import aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2NetworkAclDetails(TypedDict, closed=True):
    is_default: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether this is the default network ACL for the VPC.</p>"""
    network_acl_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the network ACL.</p>"""
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Amazon Web Services account that owns the network ACL.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC for the network ACL.</p>"""
    associations: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_acl_association_list.AwsEc2NetworkAclAssociationList"
    ]
    """<p>Associations between the network ACL and subnets.</p>"""
    entries: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list.AwsEc2NetworkAclEntryList"
    ]
    """<p>The set of rules in the network ACL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkAclDetails) -> dict:
    out: dict = {}
    if "is_default" in value:
        out["IsDefault"] = value["is_default"]
    if "network_acl_id" in value:
        out["NetworkAclId"] = value["network_acl_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "associations" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_acl_association_list

        out["Associations"] = (
            aws_sdk_securityhub.types.aws_ec2_network_acl_association_list.serialize_json(
                value["associations"]
            )
        )
    if "entries" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list

        out["Entries"] = (
            aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list.serialize_json(
                value["entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkAclDetails:
    out: AwsEc2NetworkAclDetails = {}  # type: ignore[typeddict-item]
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    if "NetworkAclId" in data:
        out["network_acl_id"] = data["NetworkAclId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Associations" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_acl_association_list

        out["associations"] = (
            aws_sdk_securityhub.types.aws_ec2_network_acl_association_list.deserialize_json(
                data["Associations"]
            )
        )
    if "Entries" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list

        out["entries"] = (
            aws_sdk_securityhub.types.aws_ec2_network_acl_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    return out
