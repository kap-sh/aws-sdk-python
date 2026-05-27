"""Generated from Smithy shape ``com.amazonaws.ec2#RequestHostIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id

RequestHostIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"
]
