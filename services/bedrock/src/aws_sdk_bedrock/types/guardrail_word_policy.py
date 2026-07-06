"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_managed_word_lists
    import aws_sdk_bedrock.types.guardrail_words


class GuardrailWordPolicy(TypedDict, closed=True):
    words: NotRequired["aws_sdk_bedrock.types.guardrail_words.GuardrailWords"]
    """<p>A list of words configured for the guardrail.</p>"""
    managed_word_lists: NotRequired[
        "aws_sdk_bedrock.types.guardrail_managed_word_lists.GuardrailManagedWordLists"
    ]
    """<p>A list of managed words configured for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicy) -> dict:
    out: dict = {}
    if "words" in value:
        import aws_sdk_bedrock.types.guardrail_words

        out["words"] = aws_sdk_bedrock.types.guardrail_words.serialize_json(
            value["words"]
        )
    if "managed_word_lists" in value:
        import aws_sdk_bedrock.types.guardrail_managed_word_lists

        out["managedWordLists"] = (
            aws_sdk_bedrock.types.guardrail_managed_word_lists.serialize_json(
                value["managed_word_lists"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicy:
    out: GuardrailWordPolicy = {}  # type: ignore[typeddict-item]
    if "words" in data:
        import aws_sdk_bedrock.types.guardrail_words

        out["words"] = aws_sdk_bedrock.types.guardrail_words.deserialize_json(
            data["words"]
        )
    if "managedWordLists" in data:
        import aws_sdk_bedrock.types.guardrail_managed_word_lists

        out["managed_word_lists"] = (
            aws_sdk_bedrock.types.guardrail_managed_word_lists.deserialize_json(
                data["managedWordLists"]
            )
        )
    return out
