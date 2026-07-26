"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook

DeploymentLifecycleHookList: TypeAlias = list[
    "capo_ecs.types.deployment_lifecycle_hook.DeploymentLifecycleHook"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookList) -> list:
    import capo_ecs.types.deployment_lifecycle_hook

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.deployment_lifecycle_hook.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentLifecycleHookList:
    import capo_ecs.types.deployment_lifecycle_hook

    out: DeploymentLifecycleHookList = []
    for item in data:
        out.append(
            capo_ecs.types.deployment_lifecycle_hook.deserialize_aws_json_1_1(item)
        )
    return out
