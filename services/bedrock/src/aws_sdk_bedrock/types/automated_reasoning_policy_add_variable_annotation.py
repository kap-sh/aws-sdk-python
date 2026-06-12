"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddVariableAnnotation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyAddVariableAnnotation(TypedDict):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the new variable. This name will be used to reference the variable in rule expressions.</p>"""
    type: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The type of the variable, which can be a built-in type (like string or number) or a custom type defined in the policy.</p>"""
    description: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description.AutomatedReasoningPolicyDefinitionVariableDescription"
    """<p>A description of what the variable represents and how it should be used in rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddVariableAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddVariableAnnotation:
    out: AutomatedReasoningPolicyAddVariableAnnotation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.name required"
        )
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.type required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.description required"
        )
    return out
