"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsDependsOnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details

AwsEcsTaskDefinitionContainerDefinitionsDependsOnList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsDependsOnList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsDependsOnList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details

    out: AwsEcsTaskDefinitionContainerDefinitionsDependsOnList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_details.deserialize_json(
                item
            )
        )
    return out
