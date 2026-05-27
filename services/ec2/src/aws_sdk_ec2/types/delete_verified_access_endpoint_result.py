"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVerifiedAccessEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint


class DeleteVerifiedAccessEndpointResult(TypedDict):
    verified_access_endpoint: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
    ]
    """<p>Details about the Verified Access endpoint.</p>"""
