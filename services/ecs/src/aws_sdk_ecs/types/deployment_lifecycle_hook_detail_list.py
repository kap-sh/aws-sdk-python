"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_detail

DeploymentLifecycleHookDetailList: TypeAlias = list[
    "aws_sdk_ecs.types.deployment_lifecycle_hook_detail.DeploymentLifecycleHookDetail"
]
