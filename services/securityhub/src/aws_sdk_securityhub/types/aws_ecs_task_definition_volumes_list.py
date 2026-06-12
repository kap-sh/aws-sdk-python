"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details

AwsEcsTaskDefinitionVolumesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details.AwsEcsTaskDefinitionVolumesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionVolumesList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionVolumesList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details

    out: AwsEcsTaskDefinitionVolumesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_details.deserialize_json(
                item
            )
        )
    return out
