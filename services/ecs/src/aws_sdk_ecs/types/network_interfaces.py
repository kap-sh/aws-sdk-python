"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.network_interface

NetworkInterfaces: TypeAlias = list[
    "aws_sdk_ecs.types.network_interface.NetworkInterface"
]
