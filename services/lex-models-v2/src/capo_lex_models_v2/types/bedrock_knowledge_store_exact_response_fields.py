"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockKnowledgeStoreExactResponseFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.answer_field


class BedrockKnowledgeStoreExactResponseFields(TypedDict, closed=True):
    answer_field: NotRequired["capo_lex_models_v2.types.answer_field.AnswerField"]
    """<p>The answer field used for an exact response from Bedrock Knowledge Store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockKnowledgeStoreExactResponseFields) -> dict:
    out: dict = {}
    if "answer_field" in value:
        out["answerField"] = value["answer_field"]
    return out


def deserialize_json(data: dict) -> BedrockKnowledgeStoreExactResponseFields:
    out: BedrockKnowledgeStoreExactResponseFields = {}  # type: ignore[typeddict-item]
    if "answerField" in data:
        out["answer_field"] = data["answerField"]
    return out
