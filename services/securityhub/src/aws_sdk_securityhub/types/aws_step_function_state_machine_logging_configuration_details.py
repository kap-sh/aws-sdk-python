"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineLoggingConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsStepFunctionStateMachineLoggingConfigurationDetails(TypedDict, closed=True):
    destinations: NotRequired[
        "aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list.AwsStepFunctionStateMachineLoggingConfigurationDestinationsList"
    ]
    """<p> An array of objects that describes where your execution history events will be logged. </p>"""
    include_execution_data: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Determines whether execution data is included in your log. When set to false, data is excluded. </p>"""
    level: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Defines which category of execution history events are logged. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineLoggingConfigurationDetails,
) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list

        out["Destinations"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list.serialize_json(
                value["destinations"]
            )
        )
    if "include_execution_data" in value:
        out["IncludeExecutionData"] = value["include_execution_data"]
    if "level" in value:
        out["Level"] = value["level"]
    return out


def deserialize_json(
    data: dict,
) -> AwsStepFunctionStateMachineLoggingConfigurationDetails:
    out: AwsStepFunctionStateMachineLoggingConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "Destinations" in data:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list

        out["destinations"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "IncludeExecutionData" in data:
        out["include_execution_data"] = data["IncludeExecutionData"]
    if "Level" in data:
        out["level"] = data["Level"]
    return out
