"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteTypeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyDeleteTypeValue(TypedDict, closed=True):
    value: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The identifier or name of the value to remove from the type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteTypeValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteTypeValue:
    out: AutomatedReasoningPolicyDeleteTypeValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteTypeValue.value required"
        )
    return out
