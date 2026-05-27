"""Generated from Smithy shape ``com.amazonaws.ec2#ThreadsPerCoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.threads_per_core

ThreadsPerCoreList: TypeAlias = list[
    "aws_sdk_ec2.types.threads_per_core.ThreadsPerCore"
]
