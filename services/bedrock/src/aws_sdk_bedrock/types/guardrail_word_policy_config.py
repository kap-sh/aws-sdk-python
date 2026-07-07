"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_managed_word_lists_config
    import aws_sdk_bedrock.types.guardrail_words_config


class GuardrailWordPolicyConfig(TypedDict, closed=True):
    words_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_words_config.GuardrailWordsConfig"
    ]
    """<p>A list of words to configure for the guardrail.</p>"""
    managed_word_lists_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_managed_word_lists_config.GuardrailManagedWordListsConfig"
    ]
    """<p>A list of managed words to configure for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyConfig) -> dict:
    out: dict = {}
    if "words_config" in value:
        import aws_sdk_bedrock.types.guardrail_words_config

        out["wordsConfig"] = (
            aws_sdk_bedrock.types.guardrail_words_config.serialize_json(
                value["words_config"]
            )
        )
    if "managed_word_lists_config" in value:
        import aws_sdk_bedrock.types.guardrail_managed_word_lists_config

        out["managedWordListsConfig"] = (
            aws_sdk_bedrock.types.guardrail_managed_word_lists_config.serialize_json(
                value["managed_word_lists_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicyConfig:
    out: GuardrailWordPolicyConfig = {}  # type: ignore[typeddict-item]
    if "wordsConfig" in data:
        import aws_sdk_bedrock.types.guardrail_words_config

        out["words_config"] = (
            aws_sdk_bedrock.types.guardrail_words_config.deserialize_json(
                data["wordsConfig"]
            )
        )
    if "managedWordListsConfig" in data:
        import aws_sdk_bedrock.types.guardrail_managed_word_lists_config

        out["managed_word_lists_config"] = (
            aws_sdk_bedrock.types.guardrail_managed_word_lists_config.deserialize_json(
                data["managedWordListsConfig"]
            )
        )
    return out
