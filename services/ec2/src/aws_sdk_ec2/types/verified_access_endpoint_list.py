"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint

VerifiedAccessEndpointList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
]
