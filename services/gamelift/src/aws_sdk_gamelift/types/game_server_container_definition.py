"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_dependency_list
    import aws_sdk_gamelift.types.container_environment_list
    import aws_sdk_gamelift.types.container_mount_point_list
    import aws_sdk_gamelift.types.container_port_configuration
    import aws_sdk_gamelift.types.image_uri_string
    import aws_sdk_gamelift.types.non_zero_and128_max_ascii_string
    import aws_sdk_gamelift.types.server_sdk_version
    import aws_sdk_gamelift.types.sha256


class GameServerContainerDefinition(TypedDict, closed=True):
    container_name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>The container definition identifier. Container names are unique within a container group definition.</p>"""
    depends_on: NotRequired[
        "aws_sdk_gamelift.types.container_dependency_list.ContainerDependencyList"
    ]
    """<p>Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.</p>"""
    mount_points: NotRequired[
        "aws_sdk_gamelift.types.container_mount_point_list.ContainerMountPointList"
    ]
    """<p>A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.</p>"""
    environment_override: NotRequired[
        "aws_sdk_gamelift.types.container_environment_list.ContainerEnvironmentList"
    ]
    r"""<p>A set of environment variables that's passed to the container on startup. See the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment\">ContainerDefinition::environment</a> parameter in the <i>Amazon Elastic Container Service API Reference</i>.</p>"""
    image_uri: NotRequired["aws_sdk_gamelift.types.image_uri_string.ImageUriString"]
    """<p>The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet. For a more specific identifier, see <code>ResolvedImageDigest</code>. </p>"""
    port_configuration: NotRequired[
        "aws_sdk_gamelift.types.container_port_configuration.ContainerPortConfiguration"
    ]
    """<p>The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's <code>ConnectionPortRange</code>. </p>"""
    resolved_image_digest: NotRequired["aws_sdk_gamelift.types.sha256.Sha256"]
    """<p>A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest. </p>"""
    server_sdk_version: NotRequired[
        "aws_sdk_gamelift.types.server_sdk_version.ServerSdkVersion"
    ]
    """<p>The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerContainerDefinition) -> dict:
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
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "port_configuration" in value:
        import aws_sdk_gamelift.types.container_port_configuration

        out["PortConfiguration"] = (
            aws_sdk_gamelift.types.container_port_configuration.serialize_aws_json_1_1(
                value["port_configuration"]
            )
        )
    if "resolved_image_digest" in value:
        out["ResolvedImageDigest"] = value["resolved_image_digest"]
    if "server_sdk_version" in value:
        out["ServerSdkVersion"] = value["server_sdk_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerContainerDefinition:
    out: GameServerContainerDefinition = {}  # type: ignore[typeddict-item]
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
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "PortConfiguration" in data:
        import aws_sdk_gamelift.types.container_port_configuration

        out["port_configuration"] = (
            aws_sdk_gamelift.types.container_port_configuration.deserialize_aws_json_1_1(
                data["PortConfiguration"]
            )
        )
    if "ResolvedImageDigest" in data:
        out["resolved_image_digest"] = data["ResolvedImageDigest"]
    if "ServerSdkVersion" in data:
        out["server_sdk_version"] = data["ServerSdkVersion"]
    return out
