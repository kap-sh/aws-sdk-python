"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfaceAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.network_interface_attachment
    import aws_sdk_ec2.types.string


class DescribeNetworkInterfaceAttributeResult(TypedDict):
    attachment: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment.NetworkInterfaceAttachment"
    ]
    """<p>The attachment (if any) of the network interface.</p>"""
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The description of the network interface.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups associated with the network interface.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    source_dest_check: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).</p>"""
