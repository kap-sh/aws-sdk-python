"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateDhcpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.defaulting_dhcp_options_id
    import aws_sdk_ec2.types.vpc_id


class AssociateDhcpOptionsRequest(TypedDict):
    dhcp_options_id: NotRequired[
        "aws_sdk_ec2.types.defaulting_dhcp_options_id.DefaultingDhcpOptionsId"
    ]
    """<p>The ID of the DHCP options set, or <code>default</code> to associate no DHCP options with the VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
