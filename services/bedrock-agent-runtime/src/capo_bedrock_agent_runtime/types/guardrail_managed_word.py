"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailManagedWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_managed_word_type
    import capo_bedrock_agent_runtime.types.guardrail_word_policy_action


class GuardrailManagedWord(TypedDict, closed=True):
    match: NotRequired["str"]
    """<p>The match details for the managed word filter in the Guardrail.</p>"""
    type: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_managed_word_type.GuardrailManagedWordType"
    ]
    """<p>The type details for the managed word filter in the Guardrail.</p>"""
    action: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    ]
    """<p>The action details for the managed word filter in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWord) -> dict:
    out: dict = {}
    if "match" in value:
        out["match"] = value["match"]
    if "type" in value:
        import capo_bedrock_agent_runtime.types.guardrail_managed_word_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_managed_word_type.serialize_json(
                value["type"]
            )
        )
    if "action" in value:
        import capo_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_word_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailManagedWord:
    out: GuardrailManagedWord = {}  # type: ignore[typeddict-item]
    if "match" in data:
        out["match"] = data["match"]
    if "type" in data:
        import capo_bedrock_agent_runtime.types.guardrail_managed_word_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_managed_word_type.deserialize_json(
                data["type"]
            )
        )
    if "action" in data:
        import capo_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_word_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
