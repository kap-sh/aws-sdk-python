"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsContainerDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_container_details

AwsEcsContainerDetailsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_container_details.AwsEcsContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsContainerDetailsList) -> list:
    import capo_securityhub.types.aws_ecs_container_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_container_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEcsContainerDetailsList:
    import capo_securityhub.types.aws_ecs_container_details

    out: AwsEcsContainerDetailsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_container_details.deserialize_json(item)
        )
    return out
