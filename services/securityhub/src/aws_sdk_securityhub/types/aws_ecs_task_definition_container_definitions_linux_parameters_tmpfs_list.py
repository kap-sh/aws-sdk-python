"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details

    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details.deserialize_json(
                item
            )
        )
    return out
