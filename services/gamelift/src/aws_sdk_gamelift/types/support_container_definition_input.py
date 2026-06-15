"""Generated from Smithy shape ``com.amazonaws.gamelift#SupportContainerDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.boolean_model
    import aws_sdk_gamelift.types.container_dependency_list
    import aws_sdk_gamelift.types.container_environment_list
    import aws_sdk_gamelift.types.container_health_check
    import aws_sdk_gamelift.types.container_memory_limit
    import aws_sdk_gamelift.types.container_mount_point_list
    import aws_sdk_gamelift.types.container_port_configuration
    import aws_sdk_gamelift.types.container_vcpu
    import aws_sdk_gamelift.types.image_uri_string
    import aws_sdk_gamelift.types.non_zero_and128_max_ascii_string


class SupportContainerDefinitionInput(TypedDict):
    container_name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>A string that uniquely identifies the container definition within a container group.</p>"""
    depends_on: NotRequired[
        "aws_sdk_gamelift.types.container_dependency_list.ContainerDependencyList"
    ]
    """<p>Establishes dependencies between this container and the status of other containers in the same container group. A container can have dependencies on multiple different containers. </p> <p>.</p> <p>You can use dependencies to establish a startup/shutdown sequence across the container group. For example, you might specify that <i>ContainerB</i> has a <code>START</code> dependency on <i>ContainerA</i>. This dependency means that <i>ContainerB</i> can't start until after <i>ContainerA</i> has started. This dependency is reversed on shutdown, which means that <i>ContainerB</i> must shut down before <i>ContainerA</i> can shut down. </p>"""
    mount_points: NotRequired[
        "aws_sdk_gamelift.types.container_mount_point_list.ContainerMountPointList"
    ]
    """<p>A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.</p>"""
    environment_override: NotRequired[
        "aws_sdk_gamelift.types.container_environment_list.ContainerEnvironmentList"
    ]
    r"""<p>A set of environment variables to pass to the container on startup. See the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment\">ContainerDefinition::environment</a> parameter in the <i>Amazon Elastic Container Service API Reference</i>. </p>"""
    essential: NotRequired["aws_sdk_gamelift.types.boolean_model.BooleanModel"]
    """<p>Flags the container as vital for the container group to function properly. If an essential container fails, the entire container group restarts. At least one support container in a per-instance container group must be essential. When flagging a container as essential, also configure a health check so that the container can signal that it's healthy. </p>"""
    health_check: NotRequired[
        "aws_sdk_gamelift.types.container_health_check.ContainerHealthCheck"
    ]
    """<p>Configuration for a non-terminal health check. A container automatically restarts if it stops functioning. With a health check, you can define additional reasons to flag a container as unhealthy and restart it. If an essential container fails a health check, the entire container group restarts. </p>"""
    image_uri: NotRequired["aws_sdk_gamelift.types.image_uri_string.ImageUriString"]
    r"""<p>The location of the container image to deploy to a container fleet. Provide an image in an Amazon Elastic Container Registry public or private repository. The repository must be in the same Amazon Web Services account and Amazon Web Services Region where you're creating the container group definition. For limits on image size, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/gamelift.html\">Amazon GameLift Servers endpoints and quotas</a>. You can use any of the following image URI formats: </p> <ul> <li> <p>Image ID only: <code>[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]</code> </p> </li> <li> <p>Image ID and digest: <code>[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]@[digest]</code> </p> </li> <li> <p>Image ID and tag: <code>[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]:[tag]</code> </p> </li> </ul>"""
    memory_hard_limit_mebibytes: NotRequired[
        "aws_sdk_gamelift.types.container_memory_limit.ContainerMemoryLimit"
    ]
    r"""<p>A specified amount of memory (in MiB) to reserve for this container. If you don't specify a container-specific memory limit, the container shares the container group's total memory allocation. </p> <p> <b>Related data type: </b> <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition</a>TotalMemoryLimitMebibytes<code></code> </p>"""
    port_configuration: NotRequired[
        "aws_sdk_gamelift.types.container_port_configuration.ContainerPortConfiguration"
    ]
    """<p>A set of ports that Amazon GameLift Servers can assign to processes in a container. The container port configuration must have enough ports for each container process that accepts inbound traffic connections. A container port configuration can have can have one or more container port ranges. Each range specifies starting and ending values as well as the supported network protocol.</p> <p>Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps each container port to an externally accessible connection port (see the container fleet property <code>ConnectionPortRange</code>). </p>"""
    vcpu: NotRequired["aws_sdk_gamelift.types.container_vcpu.ContainerVcpu"]
    r"""<p>The number of vCPU units to reserve for this container. The container can use more resources when needed, if available. If you don't reserve CPU units for this container, it shares the container group's total vCPU limit. </p> <p> <b>Related data type: </b> <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition</a> TotalCpuLimit </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportContainerDefinitionInput) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "depends_on" in value:
        import aws_sdk_gamelift.types.container_dependency_list

        out["DependsOn"] = (
            aws_sdk_gamelift.types.container_dependency_list.serialize_aws_json_1_1(
                value["depends_on"]
            )
        )
    if "mount_points" in value:
        import aws_sdk_gamelift.types.container_mount_point_list

        out["MountPoints"] = (
            aws_sdk_gamelift.types.container_mount_point_list.serialize_aws_json_1_1(
                value["mount_points"]
            )
        )
    if "environment_override" in value:
        import aws_sdk_gamelift.types.container_environment_list

        out["EnvironmentOverride"] = (
            aws_sdk_gamelift.types.container_environment_list.serialize_aws_json_1_1(
                value["environment_override"]
            )
        )
    if "essential" in value:
        out["Essential"] = value["essential"]
    if "health_check" in value:
        import aws_sdk_gamelift.types.container_health_check

        out["HealthCheck"] = (
            aws_sdk_gamelift.types.container_health_check.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "memory_hard_limit_mebibytes" in value:
        out["MemoryHardLimitMebibytes"] = value["memory_hard_limit_mebibytes"]
    if "port_configuration" in value:
        import aws_sdk_gamelift.types.container_port_configuration

        out["PortConfiguration"] = (
            aws_sdk_gamelift.types.container_port_configuration.serialize_aws_json_1_1(
                value["port_configuration"]
            )
        )
    if "vcpu" in value:
        out["Vcpu"] = value["vcpu"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportContainerDefinitionInput:
    out: SupportContainerDefinitionInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "DependsOn" in data:
        import aws_sdk_gamelift.types.container_dependency_list

        out["depends_on"] = (
            aws_sdk_gamelift.types.container_dependency_list.deserialize_aws_json_1_1(
                data["DependsOn"]
            )
        )
    if "MountPoints" in data:
        import aws_sdk_gamelift.types.container_mount_point_list

        out["mount_points"] = (
            aws_sdk_gamelift.types.container_mount_point_list.deserialize_aws_json_1_1(
                data["MountPoints"]
            )
        )
    if "EnvironmentOverride" in data:
        import aws_sdk_gamelift.types.container_environment_list

        out["environment_override"] = (
            aws_sdk_gamelift.types.container_environment_list.deserialize_aws_json_1_1(
                data["EnvironmentOverride"]
            )
        )
    if "Essential" in data:
        out["essential"] = data["Essential"]
    if "HealthCheck" in data:
        import aws_sdk_gamelift.types.container_health_check

        out["health_check"] = (
            aws_sdk_gamelift.types.container_health_check.deserialize_aws_json_1_1(
                data["HealthCheck"]
            )
        )
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "MemoryHardLimitMebibytes" in data:
        out["memory_hard_limit_mebibytes"] = data["MemoryHardLimitMebibytes"]
    if "PortConfiguration" in data:
        import aws_sdk_gamelift.types.container_port_configuration

        out["port_configuration"] = (
            aws_sdk_gamelift.types.container_port_configuration.deserialize_aws_json_1_1(
                data["PortConfiguration"]
            )
        )
    if "Vcpu" in data:
        out["vcpu"] = data["Vcpu"]
    return out
