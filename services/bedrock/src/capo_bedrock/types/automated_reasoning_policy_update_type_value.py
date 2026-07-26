"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_description
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyUpdateTypeValue(TypedDict, closed=True):
    value: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The current identifier or name of the type value to update.</p>"""
    new_value: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    ]
    """<p>The new identifier or name for the type value, if you want to rename it.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_value_description.AutomatedReasoningPolicyDefinitionTypeValueDescription"
    ]
    """<p>The new description for the type value, replacing the previous description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "new_value" in value:
        out["newValue"] = value["new_value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeValue:
    out: AutomatedReasoningPolicyUpdateTypeValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeValue.value required"
        )
    if "newValue" in data:
        out["new_value"] = data["newValue"]
    if "description" in data:
        out["description"] = data["description"]
    return out
