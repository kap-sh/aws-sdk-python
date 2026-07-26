"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineLoggingConfigurationDestinationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

AwsStepFunctionStateMachineLoggingConfigurationDestinationsList: TypeAlias = list[
    "capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineLoggingConfigurationDestinationsList,
) -> list:
    import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsStepFunctionStateMachineLoggingConfigurationDestinationsList:
    import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

    out: AwsStepFunctionStateMachineLoggingConfigurationDestinationsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.deserialize_json(
                item
            )
        )
    return out
