"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineLoggingConfigurationDestinationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

AwsStepFunctionStateMachineLoggingConfigurationDestinationsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineLoggingConfigurationDestinationsList,
) -> list:
    import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsStepFunctionStateMachineLoggingConfigurationDestinationsList:
    import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details

    out: AwsStepFunctionStateMachineLoggingConfigurationDestinationsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_details.deserialize_json(
                item
            )
        )
    return out
