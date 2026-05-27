"""Generated from Smithy shape ``com.amazonaws.ec2#TrunkInterfaceAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interface_protocol_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.trunk_interface_association_id


class TrunkInterfaceAssociation(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association_id.TrunkInterfaceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    branch_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the branch network interface.</p>"""
    trunk_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the trunk network interface.</p>"""
    interface_protocol: NotRequired[
        "aws_sdk_ec2.types.interface_protocol_type.InterfaceProtocolType"
    ]
    """<p>The interface protocol. Valid values are <code>VLAN</code> and <code>GRE</code>.</p>"""
    vlan_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN when you use the VLAN protocol.</p>"""
    gre_key: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The application key when you use the GRE protocol.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the trunk interface association.</p>"""
