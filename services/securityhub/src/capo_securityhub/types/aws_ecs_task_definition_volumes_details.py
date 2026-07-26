"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details
    import capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details
    import capo_securityhub.types.aws_ecs_task_definition_volumes_host_details
    import capo_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionVolumesDetails(TypedDict, closed=True):
    docker_volume_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails"
    ]
    """<p>Information about a Docker volume.</p>"""
    efs_volume_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails"
    ]
    """<p>Information about the Amazon Elastic File System file system that is used for task storage.</p>"""
    host: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_volumes_host_details.AwsEcsTaskDefinitionVolumesHostDetails"
    ]
    """<p>Information about a bind mount host volume.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the data volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionVolumesDetails) -> dict:
    out: dict = {}
    if "docker_volume_configuration" in value:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details

        out["DockerVolumeConfiguration"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details.serialize_json(
                value["docker_volume_configuration"]
            )
        )
    if "efs_volume_configuration" in value:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details

        out["EfsVolumeConfiguration"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details.serialize_json(
                value["efs_volume_configuration"]
            )
        )
    if "host" in value:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_host_details

        out["Host"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_host_details.serialize_json(
                value["host"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionVolumesDetails:
    out: AwsEcsTaskDefinitionVolumesDetails = {}  # type: ignore[typeddict-item]
    if "DockerVolumeConfiguration" in data:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details

        out["docker_volume_configuration"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_docker_volume_configuration_details.deserialize_json(
                data["DockerVolumeConfiguration"]
            )
        )
    if "EfsVolumeConfiguration" in data:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details

        out["efs_volume_configuration"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_details.deserialize_json(
                data["EfsVolumeConfiguration"]
            )
        )
    if "Host" in data:
        import capo_securityhub.types.aws_ecs_task_definition_volumes_host_details

        out["host"] = (
            capo_securityhub.types.aws_ecs_task_definition_volumes_host_details.deserialize_json(
                data["Host"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
