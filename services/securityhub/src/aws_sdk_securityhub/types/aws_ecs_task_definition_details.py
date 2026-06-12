"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list
    import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list
    import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list
    import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details
    import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionDetails(TypedDict):
    container_definitions: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list.AwsEcsTaskDefinitionContainerDefinitionsList"
    ]
    """<p>The container definitions that describe the containers that make up the task.</p>"""
    cpu: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The number of CPU units used by the task.Valid values are as follows:</p> <ul> <li> <p> <code>256 (.25 vCPU)</code> </p> </li> <li> <p> <code>512 (.5 vCPU)</code> </p> </li> <li> <p> <code>1024 (1 vCPU)</code> </p> </li> <li> <p> <code>2048 (2 vCPU)</code> </p> </li> <li> <p> <code>4096 (4 vCPU)</code> </p> </li> </ul>"""
    execution_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the task execution role that grants the container agent permission to make API calls on behalf of the container user.</p>"""
    family: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of a family that this task definition is registered to.</p>"""
    inference_accelerators: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list.AwsEcsTaskDefinitionInferenceAcceleratorsList"
    ]
    """<p>The Elastic Inference accelerators to use for the containers in the task.</p>"""
    ipc_mode: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The inter-process communication (IPC) resource namespace to use for the containers in the task. Valid values are as follows:</p> <ul> <li> <p> <code>host</code> </p> </li> <li> <p> <code>none</code> </p> </li> <li> <p> <code>task</code> </p> </li> </ul>"""
    memory: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The amount (in MiB) of memory used by the task. </p> <p>For tasks that are hosted on Amazon EC2, you can provide a task-level memory value or a container-level memory value. For tasks that are hosted on Fargate, you must use one of the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size\">specified values</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>, which determines your range of supported values for the <code>Cpu</code> and <code>Memory</code> parameters.</p>"""
    network_mode: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Docker networking mode to use for the containers in the task. Valid values are as follows:</p> <ul> <li> <p> <code>awsvpc</code> </p> </li> <li> <p> <code>bridge</code> </p> </li> <li> <p> <code>host</code> </p> </li> <li> <p> <code>none</code> </p> </li> </ul>"""
    pid_mode: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The process namespace to use for the containers in the task. Valid values are <code>host</code> or <code>task</code>.</p>"""
    placement_constraints: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list.AwsEcsTaskDefinitionPlacementConstraintsList"
    ]
    """<p>The placement constraint objects to use for tasks.</p>"""
    proxy_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details.AwsEcsTaskDefinitionProxyConfigurationDetails"
    ]
    """<p>The configuration details for the App Mesh proxy.</p>"""
    requires_compatibilities: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The task launch types that the task definition was validated against.</p>"""
    task_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The short name or ARN of the IAM role that grants containers in the task permission to call Amazon Web Services API operations on your behalf.</p>"""
    volumes: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list.AwsEcsTaskDefinitionVolumesList"
    ]
    """<p>The data volume definitions for the task.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The status of the task definition. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionDetails) -> dict:
    out: dict = {}
    if "container_definitions" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list

        out["ContainerDefinitions"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list.serialize_json(
                value["container_definitions"]
            )
        )
    if "cpu" in value:
        out["Cpu"] = value["cpu"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "family" in value:
        out["Family"] = value["family"]
    if "inference_accelerators" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list

        out["InferenceAccelerators"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list.serialize_json(
                value["inference_accelerators"]
            )
        )
    if "ipc_mode" in value:
        out["IpcMode"] = value["ipc_mode"]
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "network_mode" in value:
        out["NetworkMode"] = value["network_mode"]
    if "pid_mode" in value:
        out["PidMode"] = value["pid_mode"]
    if "placement_constraints" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list

        out["PlacementConstraints"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list.serialize_json(
                value["placement_constraints"]
            )
        )
    if "proxy_configuration" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details

        out["ProxyConfiguration"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details.serialize_json(
                value["proxy_configuration"]
            )
        )
    if "requires_compatibilities" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["RequiresCompatibilities"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["requires_compatibilities"]
            )
        )
    if "task_role_arn" in value:
        out["TaskRoleArn"] = value["task_role_arn"]
    if "volumes" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list

        out["Volumes"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list.serialize_json(
                value["volumes"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionDetails:
    out: AwsEcsTaskDefinitionDetails = {}  # type: ignore[typeddict-item]
    if "ContainerDefinitions" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list

        out["container_definitions"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_list.deserialize_json(
                data["ContainerDefinitions"]
            )
        )
    if "Cpu" in data:
        out["cpu"] = data["Cpu"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "Family" in data:
        out["family"] = data["Family"]
    if "InferenceAccelerators" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list

        out["inference_accelerators"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_list.deserialize_json(
                data["InferenceAccelerators"]
            )
        )
    if "IpcMode" in data:
        out["ipc_mode"] = data["IpcMode"]
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "NetworkMode" in data:
        out["network_mode"] = data["NetworkMode"]
    if "PidMode" in data:
        out["pid_mode"] = data["PidMode"]
    if "PlacementConstraints" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list

        out["placement_constraints"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_list.deserialize_json(
                data["PlacementConstraints"]
            )
        )
    if "ProxyConfiguration" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details

        out["proxy_configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_details.deserialize_json(
                data["ProxyConfiguration"]
            )
        )
    if "RequiresCompatibilities" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["requires_compatibilities"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["RequiresCompatibilities"]
            )
        )
    if "TaskRoleArn" in data:
        out["task_role_arn"] = data["TaskRoleArn"]
    if "Volumes" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list

        out["volumes"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_list.deserialize_json(
                data["Volumes"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    return out
