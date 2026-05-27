"""Generated from Smithy shape ``com.amazonaws.ec2#CoipCidr``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.string


class CoipCidr(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> An address range in a customer-owned IP address space. </p>"""
    coip_pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p> The ID of the address pool. </p>"""
    local_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the local gateway route table. </p>"""
