"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details

AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details

    out: AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_details.deserialize_json(
                item
            )
        )
    return out
