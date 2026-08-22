"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailCustomWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_word_policy_action


class GuardrailCustomWord(TypedDict, closed=True):
    match: NotRequired["str"]
    """<p>The match details for the custom word filter in the Guardrail.</p>"""
    action: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    ]
    """<p>The action details for the custom word filter in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWord) -> dict:
    out: dict = {}
    if "match" in value:
        out["match"] = value["match"]
    if "action" in value:
        import capo_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_word_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailCustomWord:
    out: GuardrailCustomWord = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        out["match"] = data["match"]
    if data.get("action") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_word_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
