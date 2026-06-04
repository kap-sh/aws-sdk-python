"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_detail

DeploymentLifecycleHookDetailList: TypeAlias = list[
    "aws_sdk_ecs.types.deployment_lifecycle_hook_detail.DeploymentLifecycleHookDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookDetailList) -> list:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.deployment_lifecycle_hook_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentLifecycleHookDetailList:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_detail

    out: DeploymentLifecycleHookDetailList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.deployment_lifecycle_hook_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
