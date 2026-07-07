"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailWordPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_custom_word_list
    import aws_sdk_bedrock_runtime.types.guardrail_managed_word_list


class GuardrailWordPolicyAssessment(TypedDict, closed=True):
    custom_words: "aws_sdk_bedrock_runtime.types.guardrail_custom_word_list.GuardrailCustomWordList"
    """<p>Custom words in the assessment.</p>"""
    managed_word_lists: "aws_sdk_bedrock_runtime.types.guardrail_managed_word_list.GuardrailManagedWordList"
    """<p>Managed word lists in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyAssessment) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_custom_word_list

    out["customWords"] = (
        aws_sdk_bedrock_runtime.types.guardrail_custom_word_list.serialize_json(
            value["custom_words"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_managed_word_list

    out["managedWordLists"] = (
        aws_sdk_bedrock_runtime.types.guardrail_managed_word_list.serialize_json(
            value["managed_word_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicyAssessment:
    out: GuardrailWordPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "customWords" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_custom_word_list

        out["custom_words"] = (
            aws_sdk_bedrock_runtime.types.guardrail_custom_word_list.deserialize_json(
                data["customWords"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailWordPolicyAssessment.custom_words required"
        )
    if "managedWordLists" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_managed_word_list

        out["managed_word_lists"] = (
            aws_sdk_bedrock_runtime.types.guardrail_managed_word_list.deserialize_json(
                data["managedWordLists"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailWordPolicyAssessment.managed_word_lists required"
        )
    return out
