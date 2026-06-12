"""Generated from Smithy shape ``com.amazonaws.batch#TaskContainerProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.environment_variables
    import aws_sdk_batch.types.firelens_configuration
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.linux_parameters
    import aws_sdk_batch.types.log_configuration
    import aws_sdk_batch.types.mount_points
    import aws_sdk_batch.types.repository_credentials
    import aws_sdk_batch.types.resource_requirements
    import aws_sdk_batch.types.secret_list
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list
    import aws_sdk_batch.types.task_container_dependency_list
    import aws_sdk_batch.types.ulimits


class TaskContainerProperties(TypedDict):
    command: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>The command that's passed to the container. This parameter maps to <code>Cmd</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>COMMAND</code> parameter to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. For more information, see <a href=\"https://docs.docker.com/engine/reference/builder/#cmd\">Dockerfile reference: CMD</a>.</p>"""
    depends_on: NotRequired[
        "aws_sdk_batch.types.task_container_dependency_list.TaskContainerDependencyList"
    ]
    """<p>A list of containers that this container depends on.</p>"""
    environment: NotRequired[
        "aws_sdk_batch.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container. This parameter maps to Env in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--env</code> parameter to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. </p> <important> <p>We don't recommend using plaintext environment variables for sensitive information, such as credential data.</p> </important> <note> <p>Environment variables cannot start with <code>AWS_BATCH</code>. This naming convention is reserved for variables that Batch sets.</p> </note>"""
    essential: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>If the essential parameter of a container is marked as <code>true</code>, and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the <code>essential</code> parameter of a container is marked as false, its failure doesn't affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.</p> <p>All jobs must have at least one essential container. If you have an application that's composed of multiple containers, group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html\">Application Architecture</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    firelens_configuration: NotRequired[
        "aws_sdk_batch.types.firelens_configuration.FirelensConfiguration"
    ]
    """<p>The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html\">Custom log</a> routing in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    image: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The image used to start a container. This string is passed directly to the Docker daemon. By default, images in the Docker Hub registry are available. Other repositories are specified with either <code>repository-url/image:tag</code> or <code>repository-url/image@digest</code>. Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to <code>Image</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <code>IMAGE</code> parameter of the <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\"> <i>docker run</i> </a>.</p>"""
    linux_parameters: NotRequired[
        "aws_sdk_batch.types.linux_parameters.LinuxParameters"
    ]
    """<p>Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html\">KernelCapabilities</a>.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_batch.types.log_configuration.LogConfiguration"
    ]
    """<p>The log configuration specification for the container.</p> <p>This parameter maps to <code>LogConfig</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <code>--log-driver</code> option to <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\">docker run</a>.</p> <p>By default, containers use the same logging driver that the Docker daemon uses. However the container can use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information about the options for different supported log drivers, see <a href=\"https://docs.docker.com/engine/admin/logging/overview/\">Configure logging drivers </a> in the <i>Docker documentation</i>.</p> <note> <p>Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the <code>LogConfiguration</code> data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.</p> </note> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version <code>--format '{{.Server.APIVersion}}'</code> </p> <note> <p>The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the <code>ECS_AVAILABLE_LOGGING_DRIVERS</code> environment variable before containers placed on that instance can use these log configuration options. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html\">Amazon ECS container agent configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    mount_points: NotRequired["aws_sdk_batch.types.mount_points.MountPoints"]
    """<p>The mount points for data volumes in your container.</p> <p>This parameter maps to <code>Volumes</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <a href=\"\">--volume</a> option to <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\">docker run</a>.</p> <p>Windows containers can mount whole directories on the same drive as <code>$env:ProgramData</code>. Windows containers can't mount directories on a different drive, and mount point can't be across drives.</p>"""
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of a container. The name can be used as a unique identifier to target your <code>dependsOn</code> and <code>Overrides</code> objects. </p>"""
    privileged: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>When this parameter is <code>true</code>, the container is given elevated privileges on the host container instance (similar to the <code>root</code> user). This parameter maps to <code>Privileged</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <code>--privileged</code> option to <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\">docker run</a>.</p> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>"""
    readonly_root_filesystem: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>When this parameter is true, the container is given read-only access to its root file system. This parameter maps to <code>ReadonlyRootfs</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <code>--read-only</code> option to <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\">docker run</a>.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    repository_credentials: NotRequired[
        "aws_sdk_batch.types.repository_credentials.RepositoryCredentials"
    ]
    """<p>The private repository authentication credentials to use.</p>"""
    resource_requirements: NotRequired[
        "aws_sdk_batch.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of a resource to assign to a container. The only supported resource is a GPU.</p>"""
    secrets: NotRequired["aws_sdk_batch.types.secret_list.SecretList"]
    """<p>The secrets to pass to the container. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html\">Specifying Sensitive Data</a> in the Amazon Elastic Container Service Developer Guide.</p>"""
    ulimits: NotRequired["aws_sdk_batch.types.ulimits.Ulimits"]
    """<p>A list of <code>ulimits</code> to set in the container. If a <code>ulimit</code> value is specified in a task definition, it overrides the default values set by Docker. This parameter maps to <code>Ulimits</code> in the <a href=\"https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.35/\">Docker Remote API</a> and the <code>--ulimit</code> option to <a href=\"https://docs.docker.com/engine/reference/run/#security-configuration\">docker run</a>.</p> <p>Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the nofile resource limit parameter which Fargate overrides. The <code>nofile</code> resource limit sets a restriction on the number of open files that a container can use. The default <code>nofile</code> soft limit is <code>1024</code> and the default hard limit is <code>65535</code>.</p> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version <code>--format '{{.Server.APIVersion}}'</code> </p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    user: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The user to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run.</p> <note> <p>When running tasks using the <code>host</code> network mode, don't run containers using the <code>root user (UID 0)</code>. We recommend using a non-root user for better security.</p> </note> <p>You can specify the <code>user</code> using the following formats. If specifying a UID or GID, you must specify it as a positive integer.</p> <ul> <li> <p> <code>user</code> </p> </li> <li> <p> <code>user:group</code> </p> </li> <li> <p> <code>uid</code> </p> </li> <li> <p> <code>uid:gid</code> </p> </li> <li> <p> <code>user:gi</code> </p> </li> <li> <p> <code>uid:group</code> </p> </li> </ul> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    start_timeout: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>Time duration (in seconds) to wait before giving up on resolving dependencies for a container. The minimum value is 2 seconds and the maximum value for Fargate is 120 seconds.</p>"""
    stop_timeout: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own. The minimum value is 2 seconds and the maximum value for Fargate is 120 seconds. If the parameter is not specified, the default value of 30 seconds is used. For tasks that use the EC2 launch type, if the <code>stopTimeout</code> parameter isn't specified, the value set for the Amazon ECS container agent configuration variable <code>ECS_CONTAINER_STOP_TIMEOUT</code> is used. If neither the <code>stopTimeout</code> parameter nor the <code>ECS_CONTAINER_STOP_TIMEOUT</code> agent configuration variable are set, then the default value of 30 seconds is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskContainerProperties) -> dict:
    out: dict = {}
    if "command" in value:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.serialize_json(
            value["command"]
        )
    if "depends_on" in value:
        import aws_sdk_batch.types.task_container_dependency_list

        out["dependsOn"] = (
            aws_sdk_batch.types.task_container_dependency_list.serialize_json(
                value["depends_on"]
            )
        )
    if "environment" in value:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.serialize_json(
            value["environment"]
        )
    if "essential" in value:
        out["essential"] = value["essential"]
    if "firelens_configuration" in value:
        import aws_sdk_batch.types.firelens_configuration

        out["firelensConfiguration"] = (
            aws_sdk_batch.types.firelens_configuration.serialize_json(
                value["firelens_configuration"]
            )
        )
    if "image" in value:
        out["image"] = value["image"]
    if "linux_parameters" in value:
        import aws_sdk_batch.types.linux_parameters

        out["linuxParameters"] = aws_sdk_batch.types.linux_parameters.serialize_json(
            value["linux_parameters"]
        )
    if "log_configuration" in value:
        import aws_sdk_batch.types.log_configuration

        out["logConfiguration"] = aws_sdk_batch.types.log_configuration.serialize_json(
            value["log_configuration"]
        )
    if "mount_points" in value:
        import aws_sdk_batch.types.mount_points

        out["mountPoints"] = aws_sdk_batch.types.mount_points.serialize_json(
            value["mount_points"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "readonly_root_filesystem" in value:
        out["readonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "repository_credentials" in value:
        import aws_sdk_batch.types.repository_credentials

        out["repositoryCredentials"] = (
            aws_sdk_batch.types.repository_credentials.serialize_json(
                value["repository_credentials"]
            )
        )
    if "resource_requirements" in value:
        import aws_sdk_batch.types.resource_requirements

        out["resourceRequirements"] = (
            aws_sdk_batch.types.resource_requirements.serialize_json(
                value["resource_requirements"]
            )
        )
    if "secrets" in value:
        import aws_sdk_batch.types.secret_list

        out["secrets"] = aws_sdk_batch.types.secret_list.serialize_json(
            value["secrets"]
        )
    if "ulimits" in value:
        import aws_sdk_batch.types.ulimits

        out["ulimits"] = aws_sdk_batch.types.ulimits.serialize_json(value["ulimits"])
    if "user" in value:
        out["user"] = value["user"]
    if "start_timeout" in value:
        out["startTimeout"] = value["start_timeout"]
    if "stop_timeout" in value:
        out["stopTimeout"] = value["stop_timeout"]
    return out


def deserialize_json(data: dict) -> TaskContainerProperties:
    out: TaskContainerProperties = {}  # type: ignore[typeddict-item]
    if "command" in data:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["command"]
        )
    if "dependsOn" in data:
        import aws_sdk_batch.types.task_container_dependency_list

        out["depends_on"] = (
            aws_sdk_batch.types.task_container_dependency_list.deserialize_json(
                data["dependsOn"]
            )
        )
    if "environment" in data:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.deserialize_json(
            data["environment"]
        )
    if "essential" in data:
        out["essential"] = data["essential"]
    if "firelensConfiguration" in data:
        import aws_sdk_batch.types.firelens_configuration

        out["firelens_configuration"] = (
            aws_sdk_batch.types.firelens_configuration.deserialize_json(
                data["firelensConfiguration"]
            )
        )
    if "image" in data:
        out["image"] = data["image"]
    if "linuxParameters" in data:
        import aws_sdk_batch.types.linux_parameters

        out["linux_parameters"] = aws_sdk_batch.types.linux_parameters.deserialize_json(
            data["linuxParameters"]
        )
    if "logConfiguration" in data:
        import aws_sdk_batch.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_batch.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "mountPoints" in data:
        import aws_sdk_batch.types.mount_points

        out["mount_points"] = aws_sdk_batch.types.mount_points.deserialize_json(
            data["mountPoints"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "privileged" in data:
        out["privileged"] = data["privileged"]
    if "readonlyRootFilesystem" in data:
        out["readonly_root_filesystem"] = data["readonlyRootFilesystem"]
    if "repositoryCredentials" in data:
        import aws_sdk_batch.types.repository_credentials

        out["repository_credentials"] = (
            aws_sdk_batch.types.repository_credentials.deserialize_json(
                data["repositoryCredentials"]
            )
        )
    if "resourceRequirements" in data:
        import aws_sdk_batch.types.resource_requirements

        out["resource_requirements"] = (
            aws_sdk_batch.types.resource_requirements.deserialize_json(
                data["resourceRequirements"]
            )
        )
    if "secrets" in data:
        import aws_sdk_batch.types.secret_list

        out["secrets"] = aws_sdk_batch.types.secret_list.deserialize_json(
            data["secrets"]
        )
    if "ulimits" in data:
        import aws_sdk_batch.types.ulimits

        out["ulimits"] = aws_sdk_batch.types.ulimits.deserialize_json(data["ulimits"])
    if "user" in data:
        out["user"] = data["user"]
    if "startTimeout" in data:
        out["start_timeout"] = data["startTimeout"]
    if "stopTimeout" in data:
        out["stop_timeout"] = data["stopTimeout"]
    return out
