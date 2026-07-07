"""Generated from Smithy shape ``com.amazonaws.pipes#EcsTaskOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.arn_or_json_path
    import aws_sdk_pipes.types.ecs_container_override_list
    import aws_sdk_pipes.types.ecs_ephemeral_storage
    import aws_sdk_pipes.types.ecs_inference_accelerator_override_list
    import aws_sdk_pipes.types.string


class EcsTaskOverride(TypedDict, closed=True):
    container_overrides: NotRequired[
        "aws_sdk_pipes.types.ecs_container_override_list.EcsContainerOverrideList"
    ]
    """<p>One or more container overrides that are sent to a task.</p>"""
    cpu: NotRequired["aws_sdk_pipes.types.string.String"]
    """<p>The cpu override for the task.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_pipes.types.ecs_ephemeral_storage.EcsEphemeralStorage"
    ]
    """<p>The ephemeral storage setting override for the task.</p> <note> <p>This parameter is only supported for tasks hosted on Fargate that use the following platform versions:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>"""
    execution_role_arn: NotRequired[
        "aws_sdk_pipes.types.arn_or_json_path.ArnOrJsonPath"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the task execution IAM role override for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html\">Amazon ECS task execution IAM role</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    inference_accelerator_overrides: NotRequired[
        "aws_sdk_pipes.types.ecs_inference_accelerator_override_list.EcsInferenceAcceleratorOverrideList"
    ]
    """<p>The Elastic Inference accelerator override for the task.</p>"""
    memory: NotRequired["aws_sdk_pipes.types.string.String"]
    """<p>The memory override for the task.</p>"""
    task_role_arn: NotRequired["aws_sdk_pipes.types.arn_or_json_path.ArnOrJsonPath"]
    r"""<p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html\">IAM Role for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTaskOverride) -> dict:
    out: dict = {}
    if "container_overrides" in value:
        import aws_sdk_pipes.types.ecs_container_override_list

        out["ContainerOverrides"] = (
            aws_sdk_pipes.types.ecs_container_override_list.serialize_json(
                value["container_overrides"]
            )
        )
    if "cpu" in value:
        out["Cpu"] = value["cpu"]
    if "ephemeral_storage" in value:
        import aws_sdk_pipes.types.ecs_ephemeral_storage

        out["EphemeralStorage"] = (
            aws_sdk_pipes.types.ecs_ephemeral_storage.serialize_json(
                value["ephemeral_storage"]
            )
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "inference_accelerator_overrides" in value:
        import aws_sdk_pipes.types.ecs_inference_accelerator_override_list

        out["InferenceAcceleratorOverrides"] = (
            aws_sdk_pipes.types.ecs_inference_accelerator_override_list.serialize_json(
                value["inference_accelerator_overrides"]
            )
        )
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "task_role_arn" in value:
        out["TaskRoleArn"] = value["task_role_arn"]
    return out


def deserialize_json(data: dict) -> EcsTaskOverride:
    out: EcsTaskOverride = {}  # type: ignore[typeddict-item]
    if "ContainerOverrides" in data:
        import aws_sdk_pipes.types.ecs_container_override_list

        out["container_overrides"] = (
            aws_sdk_pipes.types.ecs_container_override_list.deserialize_json(
                data["ContainerOverrides"]
            )
        )
    if "Cpu" in data:
        out["cpu"] = data["Cpu"]
    if "EphemeralStorage" in data:
        import aws_sdk_pipes.types.ecs_ephemeral_storage

        out["ephemeral_storage"] = (
            aws_sdk_pipes.types.ecs_ephemeral_storage.deserialize_json(
                data["EphemeralStorage"]
            )
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "InferenceAcceleratorOverrides" in data:
        import aws_sdk_pipes.types.ecs_inference_accelerator_override_list

        out["inference_accelerator_overrides"] = (
            aws_sdk_pipes.types.ecs_inference_accelerator_override_list.deserialize_json(
                data["InferenceAcceleratorOverrides"]
            )
        )
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "TaskRoleArn" in data:
        out["task_role_arn"] = data["TaskRoleArn"]
    return out
