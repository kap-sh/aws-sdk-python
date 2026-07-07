"""Generated from Smithy shape ``com.amazonaws.ecs#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.gpu_ids
    import aws_sdk_ecs.types.health_status
    import aws_sdk_ecs.types.managed_agents
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.network_interfaces
    import aws_sdk_ecs.types.neuron_device_ids
    import aws_sdk_ecs.types.string


class Container(TypedDict, closed=True):
    container_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container.</p>"""
    task_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the task.</p>"""
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The image used for the container.</p>"""
    image_digest: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image manifest digest.</p>"""
    runtime_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    last_status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The last known status of the container.</p>"""
    exit_code: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code returned from the container.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A short (1024 max characters) human-readable string to provide additional details about a running or stopped container.</p>"""
    network_bindings: NotRequired["aws_sdk_ecs.types.network_bindings.NetworkBindings"]
    """<p>The network bindings associated with the container.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ecs.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>The network interfaces associated with the container.</p>"""
    health_status: NotRequired["aws_sdk_ecs.types.health_status.HealthStatus"]
    """<p>The health status of the container. If health checks aren't configured for this container in its task definition, then it reports the health status as <code>UNKNOWN</code>.</p>"""
    managed_agents: NotRequired["aws_sdk_ecs.types.managed_agents.ManagedAgents"]
    """<p>The details of any Amazon ECS managed agents associated with the container.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The number of CPU units set for the container. The value is <code>0</code> if no value was specified in the container definition when the task definition was registered.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The hard limit (in MiB) of memory set for the container.</p>"""
    memory_reservation: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The soft limit (in MiB) of memory set for the container.</p>"""
    gpu_ids: NotRequired["aws_sdk_ecs.types.gpu_ids.GpuIds"]
    """<p>The IDs of each GPU assigned to the container.</p>"""
    neuron_device_ids: NotRequired[
        "aws_sdk_ecs.types.neuron_device_ids.NeuronDeviceIds"
    ]
    """<p>The IDs of each Neuron device assigned to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Container) -> dict:
    out: dict = {}
    if "container_arn" in value:
        out["containerArn"] = value["container_arn"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "runtime_id" in value:
        out["runtimeId"] = value["runtime_id"]
    if "last_status" in value:
        out["lastStatus"] = value["last_status"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "network_bindings" in value:
        import aws_sdk_ecs.types.network_bindings

        out["networkBindings"] = (
            aws_sdk_ecs.types.network_bindings.serialize_aws_json_1_1(
                value["network_bindings"]
            )
        )
    if "network_interfaces" in value:
        import aws_sdk_ecs.types.network_interfaces

        out["networkInterfaces"] = (
            aws_sdk_ecs.types.network_interfaces.serialize_aws_json_1_1(
                value["network_interfaces"]
            )
        )
    if "health_status" in value:
        import aws_sdk_ecs.types.health_status

        out["healthStatus"] = aws_sdk_ecs.types.health_status.serialize_aws_json_1_1(
            value["health_status"]
        )
    if "managed_agents" in value:
        import aws_sdk_ecs.types.managed_agents

        out["managedAgents"] = aws_sdk_ecs.types.managed_agents.serialize_aws_json_1_1(
            value["managed_agents"]
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "gpu_ids" in value:
        import aws_sdk_ecs.types.gpu_ids

        out["gpuIds"] = aws_sdk_ecs.types.gpu_ids.serialize_aws_json_1_1(
            value["gpu_ids"]
        )
    if "neuron_device_ids" in value:
        import aws_sdk_ecs.types.neuron_device_ids

        out["neuronDeviceIds"] = (
            aws_sdk_ecs.types.neuron_device_ids.serialize_aws_json_1_1(
                value["neuron_device_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "containerArn" in data:
        out["container_arn"] = data["containerArn"]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "image" in data:
        out["image"] = data["image"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "runtimeId" in data:
        out["runtime_id"] = data["runtimeId"]
    if "lastStatus" in data:
        out["last_status"] = data["lastStatus"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "networkBindings" in data:
        import aws_sdk_ecs.types.network_bindings

        out["network_bindings"] = (
            aws_sdk_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    if "networkInterfaces" in data:
        import aws_sdk_ecs.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_ecs.types.network_interfaces.deserialize_aws_json_1_1(
                data["networkInterfaces"]
            )
        )
    if "healthStatus" in data:
        import aws_sdk_ecs.types.health_status

        out["health_status"] = aws_sdk_ecs.types.health_status.deserialize_aws_json_1_1(
            data["healthStatus"]
        )
    if "managedAgents" in data:
        import aws_sdk_ecs.types.managed_agents

        out["managed_agents"] = (
            aws_sdk_ecs.types.managed_agents.deserialize_aws_json_1_1(
                data["managedAgents"]
            )
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "memoryReservation" in data:
        out["memory_reservation"] = data["memoryReservation"]
    if "gpuIds" in data:
        import aws_sdk_ecs.types.gpu_ids

        out["gpu_ids"] = aws_sdk_ecs.types.gpu_ids.deserialize_aws_json_1_1(
            data["gpuIds"]
        )
    if "neuronDeviceIds" in data:
        import aws_sdk_ecs.types.neuron_device_ids

        out["neuron_device_ids"] = (
            aws_sdk_ecs.types.neuron_device_ids.deserialize_aws_json_1_1(
                data["neuronDeviceIds"]
            )
        )
    return out
