"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rerank_document_type
    import capo_bedrock_agent_runtime.types.rerank_text_document


class RerankDocument(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.rerank_document_type.RerankDocumentType"
    """<p>The type of document to rerank.</p>"""
    text_document: NotRequired[
        "capo_bedrock_agent_runtime.types.rerank_text_document.RerankTextDocument"
    ]
    """<p>Contains information about a text document to rerank.</p>"""
    json_document: NotRequired["object"]
    """<p>Contains a JSON document to rerank.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankDocument) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.rerank_document_type

    out["type"] = capo_bedrock_agent_runtime.types.rerank_document_type.serialize_json(
        value["type"]
    )
    if "text_document" in value:
        import capo_bedrock_agent_runtime.types.rerank_text_document

        out["textDocument"] = (
            capo_bedrock_agent_runtime.types.rerank_text_document.serialize_json(
                value["text_document"]
            )
        )
    if "json_document" in value:
        out["jsonDocument"] = value["json_document"]
    return out


def deserialize_json(data: dict) -> RerankDocument:
    out: RerankDocument = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_agent_runtime.types.rerank_document_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.rerank_document_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("RerankDocument.type required")
    if "textDocument" in data:
        import capo_bedrock_agent_runtime.types.rerank_text_document

        out["text_document"] = (
            capo_bedrock_agent_runtime.types.rerank_text_document.deserialize_json(
                data["textDocument"]
            )
        )
    if "jsonDocument" in data:
        out["json_document"] = data["jsonDocument"]
    return out
