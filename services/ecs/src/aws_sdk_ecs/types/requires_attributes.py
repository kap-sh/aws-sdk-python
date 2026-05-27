"""Generated from Smithy shape ``com.amazonaws.ecs#RequiresAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attribute

RequiresAttributes: TypeAlias = list["aws_sdk_ecs.types.attribute.Attribute"]
