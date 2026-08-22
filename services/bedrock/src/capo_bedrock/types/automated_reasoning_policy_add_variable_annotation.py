"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddVariableAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_description
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyAddVariableAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the new variable. This name will be used to reference the variable in rule expressions.</p>"""
    type: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The type of the variable, which can be a built-in type (like string or number) or a custom type defined in the policy.</p>"""
    description: "capo_bedrock.types.automated_reasoning_policy_definition_variable_description.AutomatedReasoningPolicyDefinitionVariableDescription"
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
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.name required"
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.type required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableAnnotation.description required"
        )
    return out
