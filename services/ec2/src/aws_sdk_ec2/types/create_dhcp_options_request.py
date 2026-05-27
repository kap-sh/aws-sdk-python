"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDhcpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.new_dhcp_configuration_list
    import aws_sdk_ec2.types.tag_specification_list


class CreateDhcpOptionsRequest(TypedDict):
    dhcp_configurations: NotRequired[
        "aws_sdk_ec2.types.new_dhcp_configuration_list.NewDhcpConfigurationList"
    ]
    """<p>A DHCP configuration option.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the DHCP option.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
