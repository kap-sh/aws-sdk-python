"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details

    out: AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_details.deserialize_json(
                item
            )
        )
    return out
