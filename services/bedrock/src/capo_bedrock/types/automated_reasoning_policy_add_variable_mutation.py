"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddVariableMutation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable


class AutomatedReasoningPolicyAddVariableMutation(TypedDict, closed=True):
    variable: "capo_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"
    """<p>The variable definition that specifies the name, type, and description for the new variable being added to the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddVariableMutation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

    out["variable"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
            value["variable"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddVariableMutation:
    out: AutomatedReasoningPolicyAddVariableMutation = {}  # type: ignore[typeddict-item]
    if data.get("variable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        out["variable"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                data["variable"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddVariableMutation.variable required"
        )
    return out
