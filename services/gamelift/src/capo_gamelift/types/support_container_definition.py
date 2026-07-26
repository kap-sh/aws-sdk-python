"""Generated from Smithy shape ``com.amazonaws.gamelift#SupportContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.boolean_model
    import capo_gamelift.types.container_dependency_list
    import capo_gamelift.types.container_environment_list
    import capo_gamelift.types.container_health_check
    import capo_gamelift.types.container_memory_limit
    import capo_gamelift.types.container_mount_point_list
    import capo_gamelift.types.container_port_configuration
    import capo_gamelift.types.container_vcpu
    import capo_gamelift.types.image_uri_string
    import capo_gamelift.types.non_zero_and128_max_ascii_string
    import capo_gamelift.types.sha256


class SupportContainerDefinition(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>The container definition identifier. Container names are unique within a container group definition. </p>"""
    depends_on: NotRequired[
        "capo_gamelift.types.container_dependency_list.ContainerDependencyList"
    ]
    """<p>Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.</p>"""
    mount_points: NotRequired[
        "capo_gamelift.types.container_mount_point_list.ContainerMountPointList"
    ]
    """<p>A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.</p>"""
    environment_override: NotRequired[
        "capo_gamelift.types.container_environment_list.ContainerEnvironmentList"
    ]
    r"""<p>A set of environment variables that's passed to the container on startup. See the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment\">ContainerDefinition::environment</a> parameter in the <i>Amazon Elastic Container Service API Reference</i>.</p>"""
    essential: NotRequired["capo_gamelift.types.boolean_model.BooleanModel"]
    """<p>Indicates whether the container is vital to the container group. If an essential container fails, the entire container group restarts.</p>"""
    health_check: NotRequired[
        "capo_gamelift.types.container_health_check.ContainerHealthCheck"
    ]
    """<p>A configuration for a non-terminal health check. A support container automatically restarts if it stops functioning or if it fails this health check. </p>"""
    image_uri: NotRequired["capo_gamelift.types.image_uri_string.ImageUriString"]
    """<p>The URI to the image that Amazon GameLift Servers deploys to a container fleet. For a more specific identifier, see <code>ResolvedImageDigest</code>. </p>"""
    memory_hard_limit_mebibytes: NotRequired[
        "capo_gamelift.types.container_memory_limit.ContainerMemoryLimit"
    ]
    r"""<p>The amount of memory that Amazon GameLift Servers makes available to the container. If memory limits aren't set for an individual container, the container shares the container group's total memory allocation.</p> <p> <b>Related data type: </b> <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition TotalMemoryLimitMebibytes</a> </p>"""
    port_configuration: NotRequired[
        "capo_gamelift.types.container_port_configuration.ContainerPortConfiguration"
    ]
    """<p>A set of ports that allow access to the container from external users. Processes running in the container can bind to a one of these ports. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's <code>ConnectionPortRange</code>.</p>"""
    resolved_image_digest: NotRequired["capo_gamelift.types.sha256.Sha256"]
    """<p>A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest. </p>"""
    vcpu: NotRequired["capo_gamelift.types.container_vcpu.ContainerVcpu"]
    r"""<p>The number of vCPU units that are reserved for the container. If no resources are reserved, the container shares the total vCPU limit for the container group.</p> <p> <b>Related data type: </b> <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition TotalVcpuLimit</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportContainerDefinition) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "depends_on" in value:
        import capo_gamelift.types.container_dependency_list

        out["DependsOn"] = (
            capo_gamelift.types.container_dependency_list.serialize_aws_json_1_1(
                value["depends_on"]
            )
        )
    if "mount_points" in value:
        import capo_gamelift.types.container_mount_point_list

        out["MountPoints"] = (
            capo_gamelift.types.container_mount_point_list.serialize_aws_json_1_1(
                value["mount_points"]
            )
        )
    if "environment_override" in value:
        import capo_gamelift.types.container_environment_list

        out["EnvironmentOverride"] = (
            capo_gamelift.types.container_environment_list.serialize_aws_json_1_1(
                value["environment_override"]
            )
        )
    if "essential" in value:
        out["Essential"] = value["essential"]
    if "health_check" in value:
        import capo_gamelift.types.container_health_check

        out["HealthCheck"] = (
            capo_gamelift.types.container_health_check.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "memory_hard_limit_mebibytes" in value:
        out["MemoryHardLimitMebibytes"] = value["memory_hard_limit_mebibytes"]
    if "port_configuration" in value:
        import capo_gamelift.types.container_port_configuration

        out["PortConfiguration"] = (
            capo_gamelift.types.container_port_configuration.serialize_aws_json_1_1(
                value["port_configuration"]
            )
        )
    if "resolved_image_digest" in value:
        out["ResolvedImageDigest"] = value["resolved_image_digest"]
    if "vcpu" in value:
        out["Vcpu"] = value["vcpu"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportContainerDefinition:
    out: SupportContainerDefinition = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "DependsOn" in data:
        import capo_gamelift.types.container_dependency_list

        out["depends_on"] = (
            capo_gamelift.types.container_dependency_list.deserialize_aws_json_1_1(
                data["DependsOn"]
            )
        )
    if "MountPoints" in data:
        import capo_gamelift.types.container_mount_point_list

        out["mount_points"] = (
            capo_gamelift.types.container_mount_point_list.deserialize_aws_json_1_1(
                data["MountPoints"]
            )
        )
    if "EnvironmentOverride" in data:
        import capo_gamelift.types.container_environment_list

        out["environment_override"] = (
            capo_gamelift.types.container_environment_list.deserialize_aws_json_1_1(
                data["EnvironmentOverride"]
            )
        )
    if "Essential" in data:
        out["essential"] = data["Essential"]
    if "HealthCheck" in data:
        import capo_gamelift.types.container_health_check

        out["health_check"] = (
            capo_gamelift.types.container_health_check.deserialize_aws_json_1_1(
                data["HealthCheck"]
            )
        )
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "MemoryHardLimitMebibytes" in data:
        out["memory_hard_limit_mebibytes"] = data["MemoryHardLimitMebibytes"]
    if "PortConfiguration" in data:
        import capo_gamelift.types.container_port_configuration

        out["port_configuration"] = (
            capo_gamelift.types.container_port_configuration.deserialize_aws_json_1_1(
                data["PortConfiguration"]
            )
        )
    if "ResolvedImageDigest" in data:
        out["resolved_image_digest"] = data["ResolvedImageDigest"]
    if "Vcpu" in data:
        out["vcpu"] = data["Vcpu"]
    return out
