"""Generated from Smithy shape ``com.amazonaws.batch#ContainerProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.environment_variables
    import aws_sdk_batch.types.ephemeral_storage
    import aws_sdk_batch.types.fargate_platform_configuration
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.linux_parameters
    import aws_sdk_batch.types.log_configuration
    import aws_sdk_batch.types.mount_points
    import aws_sdk_batch.types.network_configuration
    import aws_sdk_batch.types.repository_credentials
    import aws_sdk_batch.types.resource_requirements
    import aws_sdk_batch.types.runtime_platform
    import aws_sdk_batch.types.secret_list
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list
    import aws_sdk_batch.types.ulimits
    import aws_sdk_batch.types.volumes


class ContainerProperties(TypedDict):
    image: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Required. The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with <code> <i>repository-url</i>/<i>image</i>:<i>tag</i> </code>. It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (_), colons (:), periods (.), forward slashes (/), and number signs (#). This parameter maps to <code>Image</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>IMAGE</code> parameter of <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p> <note> <p>Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.</p> </note> <ul> <li> <p>Images in Amazon ECR Public repositories use the full <code>registry/repository[:tag]</code> or <code>registry/repository[@digest]</code> naming conventions. For example, <code>public.ecr.aws/<i>registry_alias</i>/<i>my-web-app</i>:<i>latest</i> </code>.</p> </li> <li> <p>Images in Amazon ECR repositories use the full registry and repository URI (for example, <code>123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name></code>).</p> </li> <li> <p>Images in official repositories on Docker Hub use a single name (for example, <code>ubuntu</code> or <code>mongo</code>).</p> </li> <li> <p>Images in other repositories on Docker Hub are qualified with an organization name (for example, <code>amazon/amazon-ecs-agent</code>).</p> </li> <li> <p>Images in other online repositories are qualified further by a domain name (for example, <code>quay.io/assemblyline/ubuntu</code>).</p> </li> </ul>"""
    vcpus: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>This parameter is deprecated, use <code>resourceRequirements</code> to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.</p> <p>Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to <code>CpuShares</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--cpu-shares</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.</p>"""
    memory: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>This parameter is deprecated, use <code>resourceRequirements</code> to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.</p>"""
    command: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>The command that's passed to the container. This parameter maps to <code>Cmd</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>COMMAND</code> parameter to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. For more information, see <a href=\"https://docs.docker.com/engine/reference/builder/#cmd\">https://docs.docker.com/engine/reference/builder/#cmd</a>.</p>"""
    job_role_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the container can assume for Amazon Web Services permissions. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html\">IAM roles for tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    execution_role_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html\">Batch execution IAM role</a> in the <i>Batch User Guide</i>.</p>"""
    volumes: NotRequired["aws_sdk_batch.types.volumes.Volumes"]
    """<p>A list of data volumes used in a job.</p>"""
    environment: NotRequired[
        "aws_sdk_batch.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container. This parameter maps to <code>Env</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--env</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p> <important> <p>We don't recommend using plaintext environment variables for sensitive information, such as credential data.</p> </important> <note> <p>Environment variables cannot start with \"<code>AWS_BATCH</code>\". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    mount_points: NotRequired["aws_sdk_batch.types.mount_points.MountPoints"]
    """<p>The mount points for data volumes in your container. This parameter maps to <code>Volumes</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--volume</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p>"""
    readonly_root_filesystem: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>When this parameter is true, the container is given read-only access to its root file system. This parameter maps to <code>ReadonlyRootfs</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--read-only</code> option to <code>docker run</code>.</p>"""
    privileged: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>When this parameter is true, the container is given elevated permissions on the host container instance (similar to the <code>root</code> user). This parameter maps to <code>Privileged</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--privileged</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. The default value is false.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.</p> </note>"""
    ulimits: NotRequired["aws_sdk_batch.types.ulimits.Ulimits"]
    """<p>A list of <code>ulimits</code> to set in the container. This parameter maps to <code>Ulimits</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--ulimit</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.</p> </note>"""
    user: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The user name to use inside the container. This parameter maps to <code>User</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--user</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p>"""
    instance_type: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type.</p> <note> <p>This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.</p> </note>"""
    resource_requirements: NotRequired[
        "aws_sdk_batch.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of resources to assign to a container. The supported resources include <code>GPU</code>, <code>MEMORY</code>, and <code>VCPU</code>.</p>"""
    linux_parameters: NotRequired[
        "aws_sdk_batch.types.linux_parameters.LinuxParameters"
    ]
    """<p>Linux-specific modifications that are applied to the container, such as details for device mappings.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_batch.types.log_configuration.LogConfiguration"
    ]
    """<p>The log configuration specification for the container.</p> <p>This parameter maps to <code>LogConfig</code> in the <a href=\"https://docs.docker.com/engine/api/v1.23/#create-a-container\">Create a container</a> section of the <a href=\"https://docs.docker.com/engine/api/v1.23/\">Docker Remote API</a> and the <code>--log-driver</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>. By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see <a href=\"https://docs.docker.com/engine/admin/logging/overview/\">Configure logging drivers</a> in the Docker documentation.</p> <note> <p>Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html\">LogConfiguration</a> data type).</p> </note> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version | grep \"Server API version\"</code> </p> <note> <p>The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the <code>ECS_AVAILABLE_LOGGING_DRIVERS</code> environment variable before containers placed on that instance can use these log configuration options. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html\">Amazon ECS container agent configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    secrets: NotRequired["aws_sdk_batch.types.secret_list.SecretList"]
    """<p>The secrets for the container. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html\">Specifying sensitive data</a> in the <i>Batch User Guide</i>.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_batch.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.</p>"""
    fargate_platform_configuration: NotRequired[
        "aws_sdk_batch.types.fargate_platform_configuration.FargatePlatformConfiguration"
    ]
    """<p>The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.</p>"""
    enable_execute_command: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Determines whether execute command functionality is turned on for this task. If <code>true</code>, execute command functionality is turned on all the containers in the task.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_batch.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.</p>"""
    runtime_platform: NotRequired[
        "aws_sdk_batch.types.runtime_platform.RuntimePlatform"
    ]
    """<p>An object that represents the compute environment architecture for Batch jobs on Fargate.</p>"""
    repository_credentials: NotRequired[
        "aws_sdk_batch.types.repository_credentials.RepositoryCredentials"
    ]
    """<p>The private repository authentication credentials to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProperties) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "vcpus" in value:
        out["vcpus"] = value["vcpus"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "command" in value:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.serialize_json(
            value["command"]
        )
    if "job_role_arn" in value:
        out["jobRoleArn"] = value["job_role_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "volumes" in value:
        import aws_sdk_batch.types.volumes

        out["volumes"] = aws_sdk_batch.types.volumes.serialize_json(value["volumes"])
    if "environment" in value:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.serialize_json(
            value["environment"]
        )
    if "mount_points" in value:
        import aws_sdk_batch.types.mount_points

        out["mountPoints"] = aws_sdk_batch.types.mount_points.serialize_json(
            value["mount_points"]
        )
    if "readonly_root_filesystem" in value:
        out["readonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "ulimits" in value:
        import aws_sdk_batch.types.ulimits

        out["ulimits"] = aws_sdk_batch.types.ulimits.serialize_json(value["ulimits"])
    if "user" in value:
        out["user"] = value["user"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "resource_requirements" in value:
        import aws_sdk_batch.types.resource_requirements

        out["resourceRequirements"] = (
            aws_sdk_batch.types.resource_requirements.serialize_json(
                value["resource_requirements"]
            )
        )
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
    if "secrets" in value:
        import aws_sdk_batch.types.secret_list

        out["secrets"] = aws_sdk_batch.types.secret_list.serialize_json(
            value["secrets"]
        )
    if "network_configuration" in value:
        import aws_sdk_batch.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_batch.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "fargate_platform_configuration" in value:
        import aws_sdk_batch.types.fargate_platform_configuration

        out["fargatePlatformConfiguration"] = (
            aws_sdk_batch.types.fargate_platform_configuration.serialize_json(
                value["fargate_platform_configuration"]
            )
        )
    if "enable_execute_command" in value:
        out["enableExecuteCommand"] = value["enable_execute_command"]
    if "ephemeral_storage" in value:
        import aws_sdk_batch.types.ephemeral_storage

        out["ephemeralStorage"] = aws_sdk_batch.types.ephemeral_storage.serialize_json(
            value["ephemeral_storage"]
        )
    if "runtime_platform" in value:
        import aws_sdk_batch.types.runtime_platform

        out["runtimePlatform"] = aws_sdk_batch.types.runtime_platform.serialize_json(
            value["runtime_platform"]
        )
    if "repository_credentials" in value:
        import aws_sdk_batch.types.repository_credentials

        out["repositoryCredentials"] = (
            aws_sdk_batch.types.repository_credentials.serialize_json(
                value["repository_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerProperties:
    out: ContainerProperties = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "vcpus" in data:
        out["vcpus"] = data["vcpus"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "command" in data:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["command"]
        )
    if "jobRoleArn" in data:
        out["job_role_arn"] = data["jobRoleArn"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "volumes" in data:
        import aws_sdk_batch.types.volumes

        out["volumes"] = aws_sdk_batch.types.volumes.deserialize_json(data["volumes"])
    if "environment" in data:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.deserialize_json(
            data["environment"]
        )
    if "mountPoints" in data:
        import aws_sdk_batch.types.mount_points

        out["mount_points"] = aws_sdk_batch.types.mount_points.deserialize_json(
            data["mountPoints"]
        )
    if "readonlyRootFilesystem" in data:
        out["readonly_root_filesystem"] = data["readonlyRootFilesystem"]
    if "privileged" in data:
        out["privileged"] = data["privileged"]
    if "ulimits" in data:
        import aws_sdk_batch.types.ulimits

        out["ulimits"] = aws_sdk_batch.types.ulimits.deserialize_json(data["ulimits"])
    if "user" in data:
        out["user"] = data["user"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "resourceRequirements" in data:
        import aws_sdk_batch.types.resource_requirements

        out["resource_requirements"] = (
            aws_sdk_batch.types.resource_requirements.deserialize_json(
                data["resourceRequirements"]
            )
        )
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
    if "secrets" in data:
        import aws_sdk_batch.types.secret_list

        out["secrets"] = aws_sdk_batch.types.secret_list.deserialize_json(
            data["secrets"]
        )
    if "networkConfiguration" in data:
        import aws_sdk_batch.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_batch.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "fargatePlatformConfiguration" in data:
        import aws_sdk_batch.types.fargate_platform_configuration

        out["fargate_platform_configuration"] = (
            aws_sdk_batch.types.fargate_platform_configuration.deserialize_json(
                data["fargatePlatformConfiguration"]
            )
        )
    if "enableExecuteCommand" in data:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    if "ephemeralStorage" in data:
        import aws_sdk_batch.types.ephemeral_storage

        out["ephemeral_storage"] = (
            aws_sdk_batch.types.ephemeral_storage.deserialize_json(
                data["ephemeralStorage"]
            )
        )
    if "runtimePlatform" in data:
        import aws_sdk_batch.types.runtime_platform

        out["runtime_platform"] = aws_sdk_batch.types.runtime_platform.deserialize_json(
            data["runtimePlatform"]
        )
    if "repositoryCredentials" in data:
        import aws_sdk_batch.types.repository_credentials

        out["repository_credentials"] = (
            aws_sdk_batch.types.repository_credentials.deserialize_json(
                data["repositoryCredentials"]
            )
        )
    return out
