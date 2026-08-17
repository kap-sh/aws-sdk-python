"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook_stage

DeploymentLifecycleHookStageList: TypeAlias = list[
    "capo_ecs.types.deployment_lifecycle_hook_stage.DeploymentLifecycleHookStage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookStageList) -> list:
    import capo_ecs.types.deployment_lifecycle_hook_stage

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.deployment_lifecycle_hook_stage.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentLifecycleHookStageList:
    import capo_ecs.types.deployment_lifecycle_hook_stage

    out: DeploymentLifecycleHookStageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.deployment_lifecycle_hook_stage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
