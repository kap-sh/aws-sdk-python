"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestKnowledgeBaseDocumentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_document_details


class IngestKnowledgeBaseDocumentsResponse(TypedDict, closed=True):
    document_details: NotRequired[
        "capo_bedrock_agent.types.knowledge_base_document_details.KnowledgeBaseDocumentDetails"
    ]
    """<p>A list of objects, each of which contains information about the documents that were ingested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestKnowledgeBaseDocumentsResponse) -> dict:
    out: dict = {}
    if "document_details" in value:
        import capo_bedrock_agent.types.knowledge_base_document_details

        out["documentDetails"] = (
            capo_bedrock_agent.types.knowledge_base_document_details.serialize_json(
                value["document_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> IngestKnowledgeBaseDocumentsResponse:
    out: IngestKnowledgeBaseDocumentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("documentDetails") is not None:
        import capo_bedrock_agent.types.knowledge_base_document_details

        out["document_details"] = (
            capo_bedrock_agent.types.knowledge_base_document_details.deserialize_json(
                data["documentDetails"]
            )
        )
    return out
