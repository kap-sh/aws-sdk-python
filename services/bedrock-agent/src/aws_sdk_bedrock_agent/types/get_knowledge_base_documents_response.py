"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetKnowledgeBaseDocumentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_document_details


class GetKnowledgeBaseDocumentsResponse(TypedDict):
    document_details: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_document_details.KnowledgeBaseDocumentDetails"
    ]
    """<p>A list of objects, each of which contains information about the documents that were retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKnowledgeBaseDocumentsResponse) -> dict:
    out: dict = {}
    if "document_details" in value:
        import aws_sdk_bedrock_agent.types.knowledge_base_document_details

        out["documentDetails"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_document_details.serialize_json(
                value["document_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetKnowledgeBaseDocumentsResponse:
    out: GetKnowledgeBaseDocumentsResponse = {}  # type: ignore[typeddict-item]
    if "documentDetails" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_document_details

        out["document_details"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_document_details.deserialize_json(
                data["documentDetails"]
            )
        )
    return out
