"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteTypeAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name


class AutomatedReasoningPolicyDeleteTypeAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the custom type to delete from the policy. The type must not be referenced by any variables or rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteTypeAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteTypeAnnotation:
    out: AutomatedReasoningPolicyDeleteTypeAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteTypeAnnotation.name required"
        )
    return out
