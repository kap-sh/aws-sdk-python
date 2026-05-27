"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorPortRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class TrafficMirrorPortRange(TypedDict):
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The start of the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The end of the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
