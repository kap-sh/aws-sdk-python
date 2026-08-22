"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateVariableMutation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable


class AutomatedReasoningPolicyUpdateVariableMutation(TypedDict, closed=True):
    variable: "capo_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"
    """<p>The updated variable definition containing the modified name, type, or description for the existing variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateVariableMutation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_variable

    out["variable"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
            value["variable"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateVariableMutation:
    out: AutomatedReasoningPolicyUpdateVariableMutation = {}  # type: ignore[typeddict-item]
    if data.get("variable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        out["variable"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                data["variable"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateVariableMutation.variable required"
        )
    return out
