"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details
    import aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsStepFunctionStateMachineDetails(TypedDict, closed=True):
    label: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A user-defined or an auto-generated string that identifies a <code>Map</code> state. This parameter is present only if the <code>stateMachineArn</code> specified in input is a qualified state machine ARN. </p>"""
    logging_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details.AwsStepFunctionStateMachineLoggingConfigurationDetails"
    ]
    """<p> Used to set CloudWatch Logs options. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the state machine. </p>"""
    role_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. </p>"""
    state_machine_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN that identifies the state machine. </p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The current status of the state machine. </p>"""
    tracing_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details.AwsStepFunctionStateMachineTracingConfigurationDetails"
    ]
    """<p> Specifies whether X-Ray tracing is enabled. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of the state machine (STANDARD or EXPRESS). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsStepFunctionStateMachineDetails) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "logging_configuration" in value:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details

        out["LoggingConfiguration"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details.serialize_json(
                value["logging_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "state_machine_arn" in value:
        out["StateMachineArn"] = value["state_machine_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "tracing_configuration" in value:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details

        out["TracingConfiguration"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details.serialize_json(
                value["tracing_configuration"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsStepFunctionStateMachineDetails:
    out: AwsStepFunctionStateMachineDetails = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        out["label"] = data["Label"]
    if "LoggingConfiguration" in data:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details

        out["logging_configuration"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_logging_configuration_details.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StateMachineArn" in data:
        out["state_machine_arn"] = data["StateMachineArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "TracingConfiguration" in data:
        import aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details

        out["tracing_configuration"] = (
            aws_sdk_securityhub.types.aws_step_function_state_machine_tracing_configuration_details.deserialize_json(
                data["TracingConfiguration"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
