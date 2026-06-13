"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateKnowledgeBaseTemplateUriResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.knowledge_base_data


class UpdateKnowledgeBaseTemplateUriResponse(TypedDict):
    knowledge_base: NotRequired[
        "aws_sdk_qconnect.types.knowledge_base_data.KnowledgeBaseData"
    ]
    """<p>The knowledge base to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseTemplateUriResponse) -> dict:
    out: dict = {}
    if "knowledge_base" in value:
        import aws_sdk_qconnect.types.knowledge_base_data

        out["knowledgeBase"] = (
            aws_sdk_qconnect.types.knowledge_base_data.serialize_json(
                value["knowledge_base"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseTemplateUriResponse:
    out: UpdateKnowledgeBaseTemplateUriResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBase" in data:
        import aws_sdk_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            aws_sdk_qconnect.types.knowledge_base_data.deserialize_json(
                data["knowledgeBase"]
            )
        )
    return out
