"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentResourceType``."""

from typing import Literal, TypeAlias

TransitGatewayAttachmentResourceType: TypeAlias = Literal[
    "vpc",
    "vpn",
    "vpn-concentrator",
    "direct-connect-gateway",
    "connect",
    "peering",
    "tgw-peering",
    "network-function",
    "client-vpn",
]
