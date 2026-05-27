"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrFailureReason``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr_failure_code
    import aws_sdk_ec2.types.string


class IpamPoolCidrFailureReason(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_cidr_failure_code.IpamPoolCidrFailureCode"
    ]
    """<p>An error code related to why an IPAM pool CIDR failed to be provisioned.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message related to why an IPAM pool CIDR failed to be provisioned.</p>"""
