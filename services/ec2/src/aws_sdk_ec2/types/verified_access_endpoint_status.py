"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_status_code


class VerifiedAccessEndpointStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_status_code.VerifiedAccessEndpointStatusCode"
    ]
    """<p>The status code of the Verified Access endpoint.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message of the Verified Access endpoint.</p>"""
