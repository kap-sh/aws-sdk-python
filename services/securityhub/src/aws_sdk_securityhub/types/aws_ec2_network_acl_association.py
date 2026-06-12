"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkAclAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2NetworkAclAssociation(TypedDict):
    network_acl_association_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the association between the network ACL and the subnet.</p>"""
    network_acl_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the network ACL.</p>"""
    subnet_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the subnet that is associated with the network ACL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkAclAssociation) -> dict:
    out: dict = {}
    if "network_acl_association_id" in value:
        out["NetworkAclAssociationId"] = value["network_acl_association_id"]
    if "network_acl_id" in value:
        out["NetworkAclId"] = value["network_acl_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkAclAssociation:
    out: AwsEc2NetworkAclAssociation = {}  # type: ignore[typeddict-item]
    if "NetworkAclAssociationId" in data:
        out["network_acl_association_id"] = data["NetworkAclAssociationId"]
    if "NetworkAclId" in data:
        out["network_acl_id"] = data["NetworkAclId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    return out
