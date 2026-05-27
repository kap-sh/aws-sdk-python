"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.terminate_connection_status

TerminateConnectionStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.terminate_connection_status.TerminateConnectionStatus"
]
