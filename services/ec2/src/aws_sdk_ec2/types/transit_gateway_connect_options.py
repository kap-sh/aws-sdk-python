"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_value


class TransitGatewayConnectOptions(TypedDict):
    protocol: NotRequired["aws_sdk_ec2.types.protocol_value.ProtocolValue"]
    """<p>The tunnel protocol.</p>"""
