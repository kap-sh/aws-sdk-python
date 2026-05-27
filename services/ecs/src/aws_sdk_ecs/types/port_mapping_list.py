"""Generated from Smithy shape ``com.amazonaws.ecs#PortMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.port_mapping

PortMappingList: TypeAlias = list["aws_sdk_ecs.types.port_mapping.PortMapping"]
