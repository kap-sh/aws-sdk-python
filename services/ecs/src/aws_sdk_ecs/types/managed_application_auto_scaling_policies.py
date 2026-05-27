"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedApplicationAutoScalingPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_application_auto_scaling_policy

ManagedApplicationAutoScalingPolicies: TypeAlias = list[
    "aws_sdk_ecs.types.managed_application_auto_scaling_policy.ManagedApplicationAutoScalingPolicy"
]
