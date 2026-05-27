"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook

DeploymentLifecycleHookList: TypeAlias = list[
    "aws_sdk_ecs.types.deployment_lifecycle_hook.DeploymentLifecycleHook"
]
