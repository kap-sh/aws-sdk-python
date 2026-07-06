"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.rerank_document
    import aws_sdk_bedrock_agent_runtime.types.rerank_source_type


class RerankSource(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent_runtime.types.rerank_source_type.RerankSourceType"
    """<p>The type of the source.</p>"""
    inline_document_source: (
        "aws_sdk_bedrock_agent_runtime.types.rerank_document.RerankDocument"
    )
    """<p>Contains an inline definition of a source for reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankSource) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.rerank_source_type

    out["type"] = aws_sdk_bedrock_agent_runtime.types.rerank_source_type.serialize_json(
        value["type"]
    )
    import aws_sdk_bedrock_agent_runtime.types.rerank_document

    out["inlineDocumentSource"] = (
        aws_sdk_bedrock_agent_runtime.types.rerank_document.serialize_json(
            value["inline_document_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> RerankSource:
    out: RerankSource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.rerank_source_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_source_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("RerankSource.type required")
    if "inlineDocumentSource" in data:
        import aws_sdk_bedrock_agent_runtime.types.rerank_document

        out["inline_document_source"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_document.deserialize_json(
                data["inlineDocumentSource"]
            )
        )
    else:
        raise DeserializationError("RerankSource.inline_document_source required")
    return out
