"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.container_dependencies
    import aws_sdk_ecs.types.container_restart_policy
    import aws_sdk_ecs.types.daemon_linux_parameters
    import aws_sdk_ecs.types.environment_files
    import aws_sdk_ecs.types.environment_variables
    import aws_sdk_ecs.types.firelens_configuration
    import aws_sdk_ecs.types.health_check
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.log_configuration
    import aws_sdk_ecs.types.mount_point_list
    import aws_sdk_ecs.types.repository_credentials
    import aws_sdk_ecs.types.secret_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.system_controls
    import aws_sdk_ecs.types.ulimit_list


class DaemonContainerDefinition(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    image: "aws_sdk_ecs.types.string.String"
    """<p>The image used to start the container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either <code> <i>repository-url</i>/<i>image</i>:<i>tag</i> </code> or <code> <i>repository-url</i>/<i>image</i>@<i>digest</i> </code>.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is killed.</p>"""
    memory_reservation: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The soft limit (in MiB) of memory to reserve for the container.</p>"""
    repository_credentials: NotRequired[
        "aws_sdk_ecs.types.repository_credentials.RepositoryCredentials"
    ]
    """<p>The private repository authentication credentials to use.</p>"""
    health_check: NotRequired["aws_sdk_ecs.types.health_check.HealthCheck"]
    """<p>The container health check command and associated configuration parameters for the container.</p>"""
    cpu: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of <code>cpu</code> units reserved for the container.</p>"""
    essential: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If the <code>essential</code> parameter of a container is marked as <code>true</code>, and that container fails or stops for any reason, all other containers that are part of the task are stopped.</p>"""
    entry_point: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The entry point that's passed to the container.</p>"""
    command: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The command that's passed to the container.</p>"""
    working_directory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The working directory to run commands inside the container in.</p>"""
    environment_files: NotRequired[
        "aws_sdk_ecs.types.environment_files.EnvironmentFiles"
    ]
    """<p>A list of files containing the environment variables to pass to a container.</p>"""
    environment: NotRequired[
        "aws_sdk_ecs.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container.</p>"""
    secrets: NotRequired["aws_sdk_ecs.types.secret_list.SecretList"]
    """<p>The secrets to pass to the container.</p>"""
    readonly_root_filesystem: NotRequired[
        "aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>When this parameter is true, the container is given read-only access to its root file system.</p>"""
    mount_points: NotRequired["aws_sdk_ecs.types.mount_point_list.MountPointList"]
    """<p>The mount points for data volumes in your container.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_ecs.types.log_configuration.LogConfiguration"
    ]
    """<p>The log configuration specification for the container.</p>"""
    firelens_configuration: NotRequired[
        "aws_sdk_ecs.types.firelens_configuration.FirelensConfiguration"
    ]
    """<p>The FireLens configuration for the container. This is used to specify and configure a log router for container logs.</p>"""
    privileged: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, the container is given elevated privileges on the host container instance (similar to the <code>root</code> user).</p>"""
    user: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The user to use inside the container.</p>"""
    ulimits: NotRequired["aws_sdk_ecs.types.ulimit_list.UlimitList"]
    """<p>A list of <code>ulimits</code> to set in the container.</p>"""
    linux_parameters: NotRequired[
        "aws_sdk_ecs.types.daemon_linux_parameters.DaemonLinuxParameters"
    ]
    """<p>Linux-specific modifications that are applied to the container configuration, such as Linux kernel capabilities.</p>"""
    depends_on: NotRequired[
        "aws_sdk_ecs.types.container_dependencies.ContainerDependencies"
    ]
    """<p>The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition.</p>"""
    start_timeout: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before giving up on resolving dependencies for a container.</p>"""
    stop_timeout: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own.</p>"""
    system_controls: NotRequired["aws_sdk_ecs.types.system_controls.SystemControls"]
    """<p>A list of namespaced kernel parameters to set in the container.</p>"""
    interactive: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, you can deploy containerized applications that require <code>stdin</code> or a <code>tty</code> to be allocated.</p>"""
    pseudo_terminal: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, a TTY is allocated.</p>"""
    restart_policy: NotRequired[
        "aws_sdk_ecs.types.container_restart_policy.ContainerRestartPolicy"
    ]
    """<p>The restart policy for the container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task.</p>"""
