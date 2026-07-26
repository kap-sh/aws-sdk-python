"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details

    out: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_details.deserialize_json(
                item
            )
        )
    return out
