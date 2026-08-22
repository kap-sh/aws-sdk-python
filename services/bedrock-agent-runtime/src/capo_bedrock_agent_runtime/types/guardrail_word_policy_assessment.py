"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailWordPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_custom_word_list
    import capo_bedrock_agent_runtime.types.guardrail_managed_word_list


class GuardrailWordPolicyAssessment(TypedDict, closed=True):
    custom_words: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_custom_word_list.GuardrailCustomWordList"
    ]
    """<p>The custom word details for words defined in the Guardrail filter.</p>"""
    managed_word_lists: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_managed_word_list.GuardrailManagedWordList"
    ]
    """<p>The managed word lists for words defined in the Guardrail filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyAssessment) -> dict:
    out: dict = {}
    if "custom_words" in value:
        import capo_bedrock_agent_runtime.types.guardrail_custom_word_list

        out["customWords"] = (
            capo_bedrock_agent_runtime.types.guardrail_custom_word_list.serialize_json(
                value["custom_words"]
            )
        )
    if "managed_word_lists" in value:
        import capo_bedrock_agent_runtime.types.guardrail_managed_word_list

        out["managedWordLists"] = (
            capo_bedrock_agent_runtime.types.guardrail_managed_word_list.serialize_json(
                value["managed_word_lists"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicyAssessment:
    out: GuardrailWordPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("customWords") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_custom_word_list

        out["custom_words"] = (
            capo_bedrock_agent_runtime.types.guardrail_custom_word_list.deserialize_json(
                data["customWords"]
            )
        )
    if data.get("managedWordLists") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_managed_word_list

        out["managed_word_lists"] = (
            capo_bedrock_agent_runtime.types.guardrail_managed_word_list.deserialize_json(
                data["managedWordLists"]
            )
        )
    return out
