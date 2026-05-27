"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_event

ServiceEvents: TypeAlias = list["aws_sdk_ecs.types.service_event.ServiceEvent"]
