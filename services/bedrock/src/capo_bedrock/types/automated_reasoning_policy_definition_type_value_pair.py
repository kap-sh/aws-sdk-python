"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValuePair``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyDefinitionTypeValuePair(TypedDict, closed=True):
    type_name: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the custom type that contains the referenced value.</p>"""
    value_name: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The name of the specific value within the type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValuePair) -> dict:
    out: dict = {}
    out["typeName"] = value["type_name"]
    out["valueName"] = value["value_name"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionTypeValuePair:
    out: AutomatedReasoningPolicyDefinitionTypeValuePair = {}  # type: ignore[typeddict-item]
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionTypeValuePair.type_name required"
        )
    if "valueName" in data:
        out["value_name"] = data["valueName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionTypeValuePair.value_name required"
        )
    return out
