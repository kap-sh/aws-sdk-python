"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAcl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_acl_association_list
    import aws_sdk_ec2.types.network_acl_entry_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkAcl(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.network_acl_association_list.NetworkAclAssociationList"
    ]
    """<p>Any associations between the network ACL and your subnets</p>"""
    entries: NotRequired["aws_sdk_ec2.types.network_acl_entry_list.NetworkAclEntryList"]
    """<p>The entries (rules) in the network ACL.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default network ACL for the VPC.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network ACL.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the network ACL.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the network ACL.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the network ACL.</p>"""
