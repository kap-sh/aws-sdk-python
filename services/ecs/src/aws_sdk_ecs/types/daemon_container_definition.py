"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["image"] = value["image"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "repository_credentials" in value:
        import aws_sdk_ecs.types.repository_credentials

        out["repositoryCredentials"] = (
            aws_sdk_ecs.types.repository_credentials.serialize_aws_json_1_1(
                value["repository_credentials"]
            )
        )
    if "health_check" in value:
        import aws_sdk_ecs.types.health_check

        out["healthCheck"] = aws_sdk_ecs.types.health_check.serialize_aws_json_1_1(
            value["health_check"]
        )
    out["cpu"] = value.get("cpu", 0)
    if "essential" in value:
        out["essential"] = value["essential"]
    if "entry_point" in value:
        import aws_sdk_ecs.types.string_list

        out["entryPoint"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["entry_point"]
        )
    if "command" in value:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "environment_files" in value:
        import aws_sdk_ecs.types.environment_files

        out["environmentFiles"] = (
            aws_sdk_ecs.types.environment_files.serialize_aws_json_1_1(
                value["environment_files"]
            )
        )
    if "environment" in value:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "secrets" in value:
        import aws_sdk_ecs.types.secret_list

        out["secrets"] = aws_sdk_ecs.types.secret_list.serialize_aws_json_1_1(
            value["secrets"]
        )
    if "readonly_root_filesystem" in value:
        out["readonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "mount_points" in value:
        import aws_sdk_ecs.types.mount_point_list

        out["mountPoints"] = aws_sdk_ecs.types.mount_point_list.serialize_aws_json_1_1(
            value["mount_points"]
        )
    if "log_configuration" in value:
        import aws_sdk_ecs.types.log_configuration

        out["logConfiguration"] = (
            aws_sdk_ecs.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "firelens_configuration" in value:
        import aws_sdk_ecs.types.firelens_configuration

        out["firelensConfiguration"] = (
            aws_sdk_ecs.types.firelens_configuration.serialize_aws_json_1_1(
                value["firelens_configuration"]
            )
        )
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "user" in value:
        out["user"] = value["user"]
    if "ulimits" in value:
        import aws_sdk_ecs.types.ulimit_list

        out["ulimits"] = aws_sdk_ecs.types.ulimit_list.serialize_aws_json_1_1(
            value["ulimits"]
        )
    if "linux_parameters" in value:
        import aws_sdk_ecs.types.daemon_linux_parameters

        out["linuxParameters"] = (
            aws_sdk_ecs.types.daemon_linux_parameters.serialize_aws_json_1_1(
                value["linux_parameters"]
            )
        )
    if "depends_on" in value:
        import aws_sdk_ecs.types.container_dependencies

        out["dependsOn"] = (
            aws_sdk_ecs.types.container_dependencies.serialize_aws_json_1_1(
                value["depends_on"]
            )
        )
    if "start_timeout" in value:
        out["startTimeout"] = value["start_timeout"]
    if "stop_timeout" in value:
        out["stopTimeout"] = value["stop_timeout"]
    if "system_controls" in value:
        import aws_sdk_ecs.types.system_controls

        out["systemControls"] = (
            aws_sdk_ecs.types.system_controls.serialize_aws_json_1_1(
                value["system_controls"]
            )
        )
    if "interactive" in value:
        out["interactive"] = value["interactive"]
    if "pseudo_terminal" in value:
        out["pseudoTerminal"] = value["pseudo_terminal"]
    if "restart_policy" in value:
        import aws_sdk_ecs.types.container_restart_policy

        out["restartPolicy"] = (
            aws_sdk_ecs.types.container_restart_policy.serialize_aws_json_1_1(
                value["restart_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonContainerDefinition:
    out: DaemonContainerDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "image" in data:
        out["image"] = data["image"]
    else:
        raise DeserializationError("DaemonContainerDefinition.image required")
    if "memory" in data:
        out["memory"] = data["memory"]
    if "memoryReservation" in data:
        out["memory_reservation"] = data["memoryReservation"]
    if "repositoryCredentials" in data:
        import aws_sdk_ecs.types.repository_credentials

        out["repository_credentials"] = (
            aws_sdk_ecs.types.repository_credentials.deserialize_aws_json_1_1(
                data["repositoryCredentials"]
            )
        )
    if "healthCheck" in data:
        import aws_sdk_ecs.types.health_check

        out["health_check"] = aws_sdk_ecs.types.health_check.deserialize_aws_json_1_1(
            data["healthCheck"]
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    else:
        out["cpu"] = 0
    if "essential" in data:
        out["essential"] = data["essential"]
    if "entryPoint" in data:
        import aws_sdk_ecs.types.string_list

        out["entry_point"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["entryPoint"]
        )
    if "command" in data:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if "workingDirectory" in data:
        out["working_directory"] = data["workingDirectory"]
    if "environmentFiles" in data:
        import aws_sdk_ecs.types.environment_files

        out["environment_files"] = (
            aws_sdk_ecs.types.environment_files.deserialize_aws_json_1_1(
                data["environmentFiles"]
            )
        )
    if "environment" in data:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "secrets" in data:
        import aws_sdk_ecs.types.secret_list

        out["secrets"] = aws_sdk_ecs.types.secret_list.deserialize_aws_json_1_1(
            data["secrets"]
        )
    if "readonlyRootFilesystem" in data:
        out["readonly_root_filesystem"] = data["readonlyRootFilesystem"]
    if "mountPoints" in data:
        import aws_sdk_ecs.types.mount_point_list

        out["mount_points"] = (
            aws_sdk_ecs.types.mount_point_list.deserialize_aws_json_1_1(
                data["mountPoints"]
            )
        )
    if "logConfiguration" in data:
        import aws_sdk_ecs.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_ecs.types.log_configuration.deserialize_aws_json_1_1(
                data["logConfiguration"]
            )
        )
    if "firelensConfiguration" in data:
        import aws_sdk_ecs.types.firelens_configuration

        out["firelens_configuration"] = (
            aws_sdk_ecs.types.firelens_configuration.deserialize_aws_json_1_1(
                data["firelensConfiguration"]
            )
        )
    if "privileged" in data:
        out["privileged"] = data["privileged"]
    if "user" in data:
        out["user"] = data["user"]
    if "ulimits" in data:
        import aws_sdk_ecs.types.ulimit_list

        out["ulimits"] = aws_sdk_ecs.types.ulimit_list.deserialize_aws_json_1_1(
            data["ulimits"]
        )
    if "linuxParameters" in data:
        import aws_sdk_ecs.types.daemon_linux_parameters

        out["linux_parameters"] = (
            aws_sdk_ecs.types.daemon_linux_parameters.deserialize_aws_json_1_1(
                data["linuxParameters"]
            )
        )
    if "dependsOn" in data:
        import aws_sdk_ecs.types.container_dependencies

        out["depends_on"] = (
            aws_sdk_ecs.types.container_dependencies.deserialize_aws_json_1_1(
                data["dependsOn"]
            )
        )
    if "startTimeout" in data:
        out["start_timeout"] = data["startTimeout"]
    if "stopTimeout" in data:
        out["stop_timeout"] = data["stopTimeout"]
    if "systemControls" in data:
        import aws_sdk_ecs.types.system_controls

        out["system_controls"] = (
            aws_sdk_ecs.types.system_controls.deserialize_aws_json_1_1(
                data["systemControls"]
            )
        )
    if "interactive" in data:
        out["interactive"] = data["interactive"]
    if "pseudoTerminal" in data:
        out["pseudo_terminal"] = data["pseudoTerminal"]
    if "restartPolicy" in data:
        import aws_sdk_ecs.types.container_restart_policy

        out["restart_policy"] = (
            aws_sdk_ecs.types.container_restart_policy.deserialize_aws_json_1_1(
                data["restartPolicy"]
            )
        )
    return out
