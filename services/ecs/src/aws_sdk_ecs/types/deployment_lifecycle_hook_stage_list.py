"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_stage

DeploymentLifecycleHookStageList: TypeAlias = list[
    "aws_sdk_ecs.types.deployment_lifecycle_hook_stage.DeploymentLifecycleHookStage"
]
