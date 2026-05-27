"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisSecurityGroupRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.string


class AnalysisSecurityGroupRule(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation.</p>"""
    direction: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The direction. The following are the possible values:</p> <ul> <li> <p>egress</p> </li> <li> <p>ingress</p> </li> </ul>"""
    security_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group ID.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>The port range.</p>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix list ID.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol name.</p>"""
