"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectRequestBgpOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long


class TransitGatewayConnectRequestBgpOptions(TypedDict):
    peer_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The peer Autonomous System Number (ASN).</p>"""
