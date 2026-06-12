"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsUlimitsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

AwsEcsTaskDefinitionContainerDefinitionsUlimitsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsUlimitsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionContainerDefinitionsUlimitsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

    out: AwsEcsTaskDefinitionContainerDefinitionsUlimitsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.deserialize_json(
                item
            )
        )
    return out
