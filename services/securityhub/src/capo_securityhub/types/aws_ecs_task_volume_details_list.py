"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskVolumeDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_volume_details

AwsEcsTaskVolumeDetailsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_volume_details.AwsEcsTaskVolumeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskVolumeDetailsList) -> list:
    import capo_securityhub.types.aws_ecs_task_volume_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_volume_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskVolumeDetailsList:
    import capo_securityhub.types.aws_ecs_task_volume_details

    out: AwsEcsTaskVolumeDetailsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_volume_details.deserialize_json(item)
        )
    return out
