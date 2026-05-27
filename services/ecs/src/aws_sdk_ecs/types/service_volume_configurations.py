"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceVolumeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_volume_configuration

ServiceVolumeConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.service_volume_configuration.ServiceVolumeConfiguration"
]
