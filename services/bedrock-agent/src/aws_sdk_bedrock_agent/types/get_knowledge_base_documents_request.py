"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetKnowledgeBaseDocumentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.document_identifiers
    import aws_sdk_bedrock_agent.types.id


class GetKnowledgeBaseDocumentsRequest(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that is connected to the data source.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that contains the documents.</p>"""
    document_identifiers: (
        "aws_sdk_bedrock_agent.types.document_identifiers.DocumentIdentifiers"
    )
    """<p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKnowledgeBaseDocumentsRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.document_identifiers

    out["documentIdentifiers"] = (
        aws_sdk_bedrock_agent.types.document_identifiers.serialize_json(
            value["document_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetKnowledgeBaseDocumentsRequest:
    out: GetKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
    if "documentIdentifiers" in data:
        import aws_sdk_bedrock_agent.types.document_identifiers

        out["document_identifiers"] = (
            aws_sdk_bedrock_agent.types.document_identifiers.deserialize_json(
                data["documentIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "GetKnowledgeBaseDocumentsRequest.document_identifiers required"
        )
    return out
