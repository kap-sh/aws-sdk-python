"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance_field

ContainerInstanceFieldList: TypeAlias = list[
    "aws_sdk_ecs.types.container_instance_field.ContainerInstanceField"
]
