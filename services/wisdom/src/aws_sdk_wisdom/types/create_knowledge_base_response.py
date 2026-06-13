"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.knowledge_base_data


class CreateKnowledgeBaseResponse(TypedDict):
    knowledge_base: NotRequired[
        "aws_sdk_wisdom.types.knowledge_base_data.KnowledgeBaseData"
    ]
    """<p>The knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseResponse) -> dict:
    out: dict = {}
    if "knowledge_base" in value:
        import aws_sdk_wisdom.types.knowledge_base_data

        out["knowledgeBase"] = aws_sdk_wisdom.types.knowledge_base_data.serialize_json(
            value["knowledge_base"]
        )
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseResponse:
    out: CreateKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBase" in data:
        import aws_sdk_wisdom.types.knowledge_base_data

        out["knowledge_base"] = (
            aws_sdk_wisdom.types.knowledge_base_data.deserialize_json(
                data["knowledgeBase"]
            )
        )
    return out
