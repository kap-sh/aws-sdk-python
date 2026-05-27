"""Generated from Smithy shape ``com.amazonaws.ecs#Container``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.gpu_ids
    import aws_sdk_ecs.types.health_status
    import aws_sdk_ecs.types.managed_agents
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.network_interfaces
    import aws_sdk_ecs.types.neuron_device_ids
    import aws_sdk_ecs.types.string


class Container(TypedDict):
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
