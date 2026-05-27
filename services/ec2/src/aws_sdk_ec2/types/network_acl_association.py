"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class NetworkAclAssociation(TypedDict):
    network_acl_association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the association between a network ACL and a subnet.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network ACL.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
