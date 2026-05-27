"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRegistries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_registry

ServiceRegistries: TypeAlias = list[
    "aws_sdk_ecs.types.service_registry.ServiceRegistry"
]
