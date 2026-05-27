"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLogGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_log_group

ManagedLogGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_log_group.ManagedLogGroup"
]
