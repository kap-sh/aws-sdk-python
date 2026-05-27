"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringTgwInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PeeringTgwInfo(TypedDict):
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    core_network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the core network where the transit gateway peer is located.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the transit gateway.</p>"""
