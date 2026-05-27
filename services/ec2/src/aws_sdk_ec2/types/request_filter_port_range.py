"""Generated from Smithy shape ``com.amazonaws.ec2#RequestFilterPortRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port


class RequestFilterPortRange(TypedDict):
    from_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The first port in the range.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The last port in the range.</p>"""
