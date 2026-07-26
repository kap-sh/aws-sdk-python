"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details

    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_details.deserialize_json(
                item
            )
        )
    return out
