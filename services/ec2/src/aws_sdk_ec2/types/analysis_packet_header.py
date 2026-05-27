"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisPacketHeader``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_address_list
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.string


class AnalysisPacketHeader(TypedDict):
    destination_addresses: NotRequired[
        "aws_sdk_ec2.types.ip_address_list.IpAddressList"
    ]
    """<p>The destination addresses.</p>"""
    destination_port_ranges: NotRequired[
        "aws_sdk_ec2.types.port_range_list.PortRangeList"
    ]
    """<p>The destination port ranges.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    source_addresses: NotRequired["aws_sdk_ec2.types.ip_address_list.IpAddressList"]
    """<p>The source addresses.</p>"""
    source_port_ranges: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The source port ranges.</p>"""
