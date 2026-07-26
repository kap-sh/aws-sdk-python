"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_volumes_details

AwsEcsTaskDefinitionVolumesList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_volumes_details.AwsEcsTaskDefinitionVolumesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionVolumesList) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_volumes_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_volumes_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionVolumesList:
    import capo_securityhub.types.aws_ecs_task_definition_volumes_details

    out: AwsEcsTaskDefinitionVolumesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_volumes_details.deserialize_json(
                item
            )
        )
    return out
