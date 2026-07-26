"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailCustomWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_word_policy_action


class GuardrailCustomWord(TypedDict, closed=True):
    match: "str"
    """<p>The match for the custom word.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    """<p>The action for the custom word.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether custom word content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWord) -> dict:
    out: dict = {}
    out["match"] = value["match"]
    import capo_bedrock_runtime.types.guardrail_word_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_word_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailCustomWord:
    out: GuardrailCustomWord = {}  # type: ignore[typeddict-item]
    if "match" in data:
        out["match"] = data["match"]
    else:
        raise DeserializationError("GuardrailCustomWord.match required")
    if "action" in data:
        import capo_bedrock_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_word_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailCustomWord.action required")
    if "detected" in data:
        out["detected"] = data["detected"]
    return out
