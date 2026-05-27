"""Generated from Smithy shape ``com.amazonaws.ecs#DevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.device

DevicesList: TypeAlias = list["aws_sdk_ecs.types.device.Device"]
