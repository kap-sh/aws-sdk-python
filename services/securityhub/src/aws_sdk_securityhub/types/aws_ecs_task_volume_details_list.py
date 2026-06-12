"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskVolumeDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_volume_details

AwsEcsTaskVolumeDetailsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_volume_details.AwsEcsTaskVolumeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskVolumeDetailsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_volume_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_volume_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskVolumeDetailsList:
    import aws_sdk_securityhub.types.aws_ecs_task_volume_details

    out: AwsEcsTaskVolumeDetailsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_volume_details.deserialize_json(item)
        )
    return out
