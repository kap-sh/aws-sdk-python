"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_stage

DeploymentLifecycleHookStageList: TypeAlias = list[
    "aws_sdk_ecs.types.deployment_lifecycle_hook_stage.DeploymentLifecycleHookStage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookStageList) -> list:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_stage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.deployment_lifecycle_hook_stage.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentLifecycleHookStageList:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_stage

    out: DeploymentLifecycleHookStageList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.deployment_lifecycle_hook_stage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
