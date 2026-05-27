"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class NetworkInterface(TypedDict):
    attachment_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The attachment ID for the network interface.</p>"""
    private_ipv4_address: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The private IPv4 address for the network interface.</p>"""
    ipv6_address: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The private IPv6 address for the network interface.</p>"""
