"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnEndpointAttributeStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_attribute_status_code
    import aws_sdk_ec2.types.string


class ClientVpnEndpointAttributeStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_attribute_status_code.ClientVpnEndpointAttributeStatusCode"
    ]
    """<p>The status code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message.</p>"""
