"""Generated from Smithy shape ``com.amazonaws.ec2#RequestHostIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id

RequestHostIdList: TypeAlias = list[
    "aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"
]
