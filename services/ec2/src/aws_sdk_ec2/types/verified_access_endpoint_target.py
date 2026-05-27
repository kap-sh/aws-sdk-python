"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_id


class VerifiedAccessEndpointTarget(TypedDict):
    verified_access_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
    ]
    """<p>The ID of the Verified Access endpoint.</p>"""
    verified_access_endpoint_target_ip_address: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The IP address of the target.</p>"""
    verified_access_endpoint_target_dns: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the target.</p>"""
