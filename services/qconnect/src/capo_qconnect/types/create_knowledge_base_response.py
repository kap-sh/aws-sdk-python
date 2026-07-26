"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_data


class CreateKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base: NotRequired[
        "capo_qconnect.types.knowledge_base_data.KnowledgeBaseData"
    ]
    """<p>The knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseResponse) -> dict:
    out: dict = {}
    if "knowledge_base" in value:
        import capo_qconnect.types.knowledge_base_data

        out["knowledgeBase"] = capo_qconnect.types.knowledge_base_data.serialize_json(
            value["knowledge_base"]
        )
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseResponse:
    out: CreateKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBase" in data:
        import capo_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            capo_qconnect.types.knowledge_base_data.deserialize_json(
                data["knowledgeBase"]
            )
        )
    return out
