"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_security_group

ManagedSecurityGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_security_group.ManagedSecurityGroup"
]
