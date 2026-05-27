"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_target_group

ManagedTargetGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_target_group.ManagedTargetGroup"
]
