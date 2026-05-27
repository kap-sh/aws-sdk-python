"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_definition

DaemonContainerDefinitionList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_container_definition.DaemonContainerDefinition"
]
