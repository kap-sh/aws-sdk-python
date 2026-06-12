"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsContainerDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_container_details

AwsEcsContainerDetailsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_container_details.AwsEcsContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsContainerDetailsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_container_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_container_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEcsContainerDetailsList:
    import aws_sdk_securityhub.types.aws_ecs_container_details

    out: AwsEcsContainerDetailsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_container_details.deserialize_json(item)
        )
    return out
