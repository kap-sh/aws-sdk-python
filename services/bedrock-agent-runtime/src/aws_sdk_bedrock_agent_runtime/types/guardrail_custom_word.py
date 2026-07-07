"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailCustomWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action


class GuardrailCustomWord(TypedDict, closed=True):
    match: NotRequired["str"]
    """<p>The match details for the custom word filter in the Guardrail.</p>"""
    action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    ]
    """<p>The action details for the custom word filter in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWord) -> dict:
    out: dict = {}
    if "match" in value:
        out["match"] = value["match"]
    if "action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailCustomWord:
    out: GuardrailCustomWord = {}  # type: ignore[typeddict-item]
    if "match" in data:
        out["match"] = data["match"]
    if "action" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
