"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.resource_requirement

ResourceRequirements: TypeAlias = list[
    "aws_sdk_ecs.types.resource_requirement.ResourceRequirement"
]
