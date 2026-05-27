"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint_id

VerifiedAccessEndpointIdList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
]
