"""Generated from Smithy shape ``com.amazonaws.ecs#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachments
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.connectivity
    import aws_sdk_ecs.types.containers
    import aws_sdk_ecs.types.ephemeral_storage
    import aws_sdk_ecs.types.health_status
    import aws_sdk_ecs.types.inference_accelerators
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.long
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_ephemeral_storage
    import aws_sdk_ecs.types.task_override
    import aws_sdk_ecs.types.task_stop_code
    import aws_sdk_ecs.types.timestamp


class Task(TypedDict, closed=True):
    attachments: NotRequired["aws_sdk_ecs.types.attachments.Attachments"]
    """<p>The Elastic Network Adapter that's associated with the task if the task uses the <code>awsvpc</code> network mode.</p>"""
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>The attributes of the task</p>"""
    availability_zone: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Availability Zone for the task.</p>"""
    capacity_provider_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The capacity provider that's associated with the task.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the task.</p>"""
    connectivity: NotRequired["aws_sdk_ecs.types.connectivity.Connectivity"]
    """<p>The connectivity status of a task.</p>"""
    connectivity_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task last went into <code>CONNECTED</code> status.</p>"""
    container_instance_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the container instances that host the task.</p>"""
    containers: NotRequired["aws_sdk_ecs.types.containers.Containers"]
    """<p>The containers that's associated with the task.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units (for example, <code>1024</code>). It can also be expressed as a string using vCPUs (for example, <code>1 vCPU</code> or <code>1 vcpu</code>). String values are converted to an integer that indicates the CPU units when the task definition is registered.</p> <p>If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). If you do not specify a value, the parameter is ignored.</p> <p>This field is required for Fargate. For information about the valid values, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size\">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task was created. More specifically, it's for the time when the task entered the <code>PENDING</code> state.</p>"""
    desired_status: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The desired status of the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html\">Task Lifecycle</a>.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether execute command functionality is turned on for this task. If <code>true</code>, execute command functionality is turned on all the containers in the task.</p>"""
    execution_stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task execution stopped.</p>"""
    group: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the task group that's associated with the task.</p>"""
    health_status: NotRequired["aws_sdk_ecs.types.health_status.HealthStatus"]
    """<p>The health status for the task. It's determined by the health of the essential containers in the task. If all essential containers in the task are reporting as <code>HEALTHY</code>, the task status also reports as <code>HEALTHY</code>. If any essential containers in the task are reporting as <code>UNHEALTHY</code> or <code>UNKNOWN</code>, the task status also reports as <code>UNHEALTHY</code> or <code>UNKNOWN</code>.</p> <note> <p>The Amazon ECS container agent doesn't monitor or report on Docker health checks that are embedded in a container image and not specified in the container definition. For example, this includes those specified in a parent image or from the image's Dockerfile. Health check parameters that are specified in a container definition override any Docker health checks that are found in the container image.</p> </note>"""
    inference_accelerators: NotRequired[
        "aws_sdk_ecs.types.inference_accelerators.InferenceAccelerators"
    ]
    """<p>The Elastic Inference accelerator that's associated with the task.</p>"""
    last_status: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The last known status for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html\">Task Lifecycle</a>.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    r"""<p>The infrastructure where your task runs on. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) that the task uses as expressed in a task definition. It can be expressed as an integer using MiB (for example, <code>1024</code>). If it's expressed as a string using GB (for example, <code>1GB</code> or <code>1 GB</code>), it's converted to an integer indicating the MiB when the task definition is registered.</p> <p>If you use the EC2 launch type, this field is optional.</p> <p>If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines the range of supported values for the <code>cpu</code> parameter.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>"""
    overrides: NotRequired["aws_sdk_ecs.types.task_override.TaskOverride"]
    """<p>One or more container overrides.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The platform version where your task runs on. A platform version is only specified for tasks that use the Fargate launch type. If you didn't specify one, the <code>LATEST</code> platform version is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The operating system that your tasks are running on. A platform family is specified only for tasks that use the Fargate launch type. </p> <p> All tasks that run as part of this service must use the same <code>platformFamily</code> value as the service (for example, <code>LINUX.</code>).</p>"""
    pull_started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the container image pull began.</p>"""
    pull_stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the container image pull completed.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task started. More specifically, it's for the time when the task transitioned from the <code>PENDING</code> state to the <code>RUNNING</code> state.</p>"""
    started_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The tag specified when a task is started. If an Amazon ECS service started the task, the <code>startedBy</code> parameter contains the deployment ID of that service.</p>"""
    stop_code: NotRequired["aws_sdk_ecs.types.task_stop_code.TaskStopCode"]
    r"""<p>The stop code indicating why a task was stopped. The <code>stoppedReason</code> might contain additional details. </p> <p>For more information about stop code, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-error-codes.html\">Stopped tasks error codes</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task was stopped. More specifically, it's for the time when the task transitioned from the <code>RUNNING</code> state to the <code>STOPPED</code> state.</p>"""
    stopped_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason that the task was stopped.</p>"""
    stopping_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task stops. More specifically, it's for the time when the task transitions from the <code>RUNNING</code> state to <code>STOPPING</code>.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task to help you categorize and organize the task. Each tag consists of a key and an optional value. You define both the key and value.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    task_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the task definition that creates the task.</p>"""
    version: "aws_sdk_ecs.types.long.Long"
    """<p>The version counter for the task. Every time a task experiences a change that starts a CloudWatch event, the version counter is incremented. If you replicate your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actions with the version reported in CloudWatch Events for the task (inside the <code>detail</code> object) to verify that the version in your event stream is current.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The ephemeral storage settings for the task.</p>"""
    fargate_ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.task_ephemeral_storage.TaskEphemeralStorage"
    ]
    """<p>The Fargate ephemeral storage settings for the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Task) -> dict:
    out: dict = {}
    if "attachments" in value:
        import aws_sdk_ecs.types.attachments

        out["attachments"] = aws_sdk_ecs.types.attachments.serialize_aws_json_1_1(
            value["attachments"]
        )
    if "attributes" in value:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "capacity_provider_name" in value:
        out["capacityProviderName"] = value["capacity_provider_name"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "connectivity" in value:
        import aws_sdk_ecs.types.connectivity

        out["connectivity"] = aws_sdk_ecs.types.connectivity.serialize_aws_json_1_1(
            value["connectivity"]
        )
    if "connectivity_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["connectivityAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["connectivity_at"]
        )
    if "container_instance_arn" in value:
        out["containerInstanceArn"] = value["container_instance_arn"]
    if "containers" in value:
        import aws_sdk_ecs.types.containers

        out["containers"] = aws_sdk_ecs.types.containers.serialize_aws_json_1_1(
            value["containers"]
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "desired_status" in value:
        out["desiredStatus"] = value["desired_status"]
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "execution_stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["executionStoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["execution_stopped_at"]
        )
    if "group" in value:
        out["group"] = value["group"]
    if "health_status" in value:
        import aws_sdk_ecs.types.health_status

        out["healthStatus"] = aws_sdk_ecs.types.health_status.serialize_aws_json_1_1(
            value["health_status"]
        )
    if "inference_accelerators" in value:
        import aws_sdk_ecs.types.inference_accelerators

        out["inferenceAccelerators"] = (
            aws_sdk_ecs.types.inference_accelerators.serialize_aws_json_1_1(
                value["inference_accelerators"]
            )
        )
    if "last_status" in value:
        out["lastStatus"] = value["last_status"]
    if "launch_type" in value:
        import aws_sdk_ecs.types.launch_type

        out["launchType"] = aws_sdk_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "memory" in value:
        out["memory"] = value["memory"]
    if "overrides" in value:
        import aws_sdk_ecs.types.task_override

        out["overrides"] = aws_sdk_ecs.types.task_override.serialize_aws_json_1_1(
            value["overrides"]
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "platform_family" in value:
        out["platformFamily"] = value["platform_family"]
    if "pull_started_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["pullStartedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["pull_started_at"]
        )
    if "pull_stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["pullStoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["pull_stopped_at"]
        )
    if "started_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["startedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "stop_code" in value:
        import aws_sdk_ecs.types.task_stop_code

        out["stopCode"] = aws_sdk_ecs.types.task_stop_code.serialize_aws_json_1_1(
            value["stop_code"]
        )
    if "stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["stoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stopped_at"]
        )
    if "stopped_reason" in value:
        out["stoppedReason"] = value["stopped_reason"]
    if "stopping_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["stoppingAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stopping_at"]
        )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    out["version"] = value.get("version", 0)
    if "ephemeral_storage" in value:
        import aws_sdk_ecs.types.ephemeral_storage

        out["ephemeralStorage"] = (
            aws_sdk_ecs.types.ephemeral_storage.serialize_aws_json_1_1(
                value["ephemeral_storage"]
            )
        )
    if "fargate_ephemeral_storage" in value:
        import aws_sdk_ecs.types.task_ephemeral_storage

        out["fargateEphemeralStorage"] = (
            aws_sdk_ecs.types.task_ephemeral_storage.serialize_aws_json_1_1(
                value["fargate_ephemeral_storage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if "attachments" in data:
        import aws_sdk_ecs.types.attachments

        out["attachments"] = aws_sdk_ecs.types.attachments.deserialize_aws_json_1_1(
            data["attachments"]
        )
    if "attributes" in data:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "capacityProviderName" in data:
        out["capacity_provider_name"] = data["capacityProviderName"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "connectivity" in data:
        import aws_sdk_ecs.types.connectivity

        out["connectivity"] = aws_sdk_ecs.types.connectivity.deserialize_aws_json_1_1(
            data["connectivity"]
        )
    if "connectivityAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["connectivity_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["connectivityAt"]
        )
    if "containerInstanceArn" in data:
        out["container_instance_arn"] = data["containerInstanceArn"]
    if "containers" in data:
        import aws_sdk_ecs.types.containers

        out["containers"] = aws_sdk_ecs.types.containers.deserialize_aws_json_1_1(
            data["containers"]
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "desiredStatus" in data:
        out["desired_status"] = data["desiredStatus"]
    if "enableExecuteCommand" in data:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if "executionStoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["execution_stopped_at"] = (
            aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
                data["executionStoppedAt"]
            )
        )
    if "group" in data:
        out["group"] = data["group"]
    if "healthStatus" in data:
        import aws_sdk_ecs.types.health_status

        out["health_status"] = aws_sdk_ecs.types.health_status.deserialize_aws_json_1_1(
            data["healthStatus"]
        )
    if "inferenceAccelerators" in data:
        import aws_sdk_ecs.types.inference_accelerators

        out["inference_accelerators"] = (
            aws_sdk_ecs.types.inference_accelerators.deserialize_aws_json_1_1(
                data["inferenceAccelerators"]
            )
        )
    if "lastStatus" in data:
        out["last_status"] = data["lastStatus"]
    if "launchType" in data:
        import aws_sdk_ecs.types.launch_type

        out["launch_type"] = aws_sdk_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if "memory" in data:
        out["memory"] = data["memory"]
    if "overrides" in data:
        import aws_sdk_ecs.types.task_override

        out["overrides"] = aws_sdk_ecs.types.task_override.deserialize_aws_json_1_1(
            data["overrides"]
        )
    if "platformVersion" in data:
        out["platform_version"] = data["platformVersion"]
    if "platformFamily" in data:
        out["platform_family"] = data["platformFamily"]
    if "pullStartedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["pull_started_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["pullStartedAt"]
        )
    if "pullStoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["pull_stopped_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["pullStoppedAt"]
        )
    if "startedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["started_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if "startedBy" in data:
        out["started_by"] = data["startedBy"]
    if "stopCode" in data:
        import aws_sdk_ecs.types.task_stop_code

        out["stop_code"] = aws_sdk_ecs.types.task_stop_code.deserialize_aws_json_1_1(
            data["stopCode"]
        )
    if "stoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["stopped_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stoppedAt"]
        )
    if "stoppedReason" in data:
        out["stopped_reason"] = data["stoppedReason"]
    if "stoppingAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["stopping_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stoppingAt"]
        )
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "taskDefinitionArn" in data:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if "ephemeralStorage" in data:
        import aws_sdk_ecs.types.ephemeral_storage

        out["ephemeral_storage"] = (
            aws_sdk_ecs.types.ephemeral_storage.deserialize_aws_json_1_1(
                data["ephemeralStorage"]
            )
        )
    if "fargateEphemeralStorage" in data:
        import aws_sdk_ecs.types.task_ephemeral_storage

        out["fargate_ephemeral_storage"] = (
            aws_sdk_ecs.types.task_ephemeral_storage.deserialize_aws_json_1_1(
                data["fargateEphemeralStorage"]
            )
        )
    return out
