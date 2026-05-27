"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint_target

VerifiedAccessEndpointTargetList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_endpoint_target.VerifiedAccessEndpointTarget"
]
