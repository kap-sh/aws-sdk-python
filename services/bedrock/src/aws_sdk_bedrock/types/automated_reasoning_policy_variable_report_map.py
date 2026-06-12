"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyVariableReportMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report

AutomatedReasoningPolicyVariableReportMap: TypeAlias = dict[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName",
    "aws_sdk_bedrock.types.automated_reasoning_policy_variable_report.AutomatedReasoningPolicyVariableReport",
]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: AutomatedReasoningPolicyVariableReportMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report

        out[key] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_variable_report.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyVariableReportMap:
    out: AutomatedReasoningPolicyVariableReportMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report

        out[key] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_variable_report.deserialize_json(
                value
            )
        )
    return out
