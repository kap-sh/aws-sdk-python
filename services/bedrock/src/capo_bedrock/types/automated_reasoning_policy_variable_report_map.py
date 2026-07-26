"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyVariableReportMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name
    import capo_bedrock.types.automated_reasoning_policy_variable_report

AutomatedReasoningPolicyVariableReportMap: TypeAlias = dict[
    "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName",
    "capo_bedrock.types.automated_reasoning_policy_variable_report.AutomatedReasoningPolicyVariableReport",
]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: AutomatedReasoningPolicyVariableReportMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock.types.automated_reasoning_policy_variable_report

        out[key] = (
            capo_bedrock.types.automated_reasoning_policy_variable_report.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyVariableReportMap:
    out: AutomatedReasoningPolicyVariableReportMap = {}
    for key, value in data.items():
        import capo_bedrock.types.automated_reasoning_policy_variable_report

        out[key] = (
            capo_bedrock.types.automated_reasoning_policy_variable_report.deserialize_json(
                value
            )
        )
    return out
