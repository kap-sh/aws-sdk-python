"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionVariable``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyDefinitionVariable(TypedDict):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the variable. Use descriptive names that clearly indicate the concept being represented.</p>"""
    type: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The data type of the variable. Valid types include bool, int, real, enum, and custom types that you can provide.</p>"""
    description: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description.AutomatedReasoningPolicyDefinitionVariableDescription"
    """<p>The description of the variable that explains what it represents and how users might refer to it. Clear and comprehensive descriptions are essential for accurate natural language translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionVariable:
    out: AutomatedReasoningPolicyDefinitionVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionVariable.name required"
        )
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionVariable.type required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionVariable.description required"
        )
    return out
