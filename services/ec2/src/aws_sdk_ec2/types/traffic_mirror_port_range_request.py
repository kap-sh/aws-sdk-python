"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorPortRangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class TrafficMirrorPortRangeRequest(TypedDict):
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The first port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The last port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
