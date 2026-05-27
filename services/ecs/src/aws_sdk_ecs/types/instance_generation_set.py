"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceGenerationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_generation

InstanceGenerationSet: TypeAlias = list[
    "aws_sdk_ecs.types.instance_generation.InstanceGeneration"
]
