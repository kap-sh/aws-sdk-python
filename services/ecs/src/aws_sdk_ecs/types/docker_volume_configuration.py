"""Generated from Smithy shape ``com.amazonaws.ecs#DockerVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.scope
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_map


class DockerVolumeConfiguration(TypedDict):
    scope: NotRequired["aws_sdk_ecs.types.scope.Scope"]
    """<p>The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a <code>task</code> are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as <code>shared</code> persist after the task stops.</p>"""
    autoprovision: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the Docker volume is created if it doesn't already exist.</p> <note> <p>This field is only used if the <code>scope</code> is <code>shared</code>.</p> </note>"""
    driver: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use <code>docker plugin ls</code> to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. This parameter maps to <code>Driver</code> in the docker container create command and the <code>xxdriver</code> option to docker volume create.</p>"""
    driver_opts: NotRequired["aws_sdk_ecs.types.string_map.StringMap"]
    """<p>A map of Docker driver-specific options passed through. This parameter maps to <code>DriverOpts</code> in the docker create-volume command and the <code>xxopt</code> option to docker volume create.</p>"""
    labels: NotRequired["aws_sdk_ecs.types.string_map.StringMap"]
    """<p>Custom metadata to add to your Docker volume. This parameter maps to <code>Labels</code> in the docker container create command and the <code>xxlabel</code> option to docker volume create.</p>"""
