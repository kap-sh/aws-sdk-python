"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointPortRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint_port_number


class VerifiedAccessEndpointPortRange(TypedDict):
    from_port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The start of the port range.</p>"""
    to_port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The end of the port range.</p>"""
