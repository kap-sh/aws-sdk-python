"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.rerank_document


class RerankResult(TypedDict):
    index: "int"
    """<p>The original index of the document from the input sources array.</p>"""
    relevance_score: "float"
    """<p>The relevance score of the document.</p>"""
    document: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.rerank_document.RerankDocument"
    ]
    """<p>Contains information about the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankResult) -> dict:
    out: dict = {}
    out["index"] = value["index"]
    out["relevanceScore"] = value["relevance_score"]
    if "document" in value:
        import aws_sdk_bedrock_agent_runtime.types.rerank_document

        out["document"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_document.serialize_json(
                value["document"]
            )
        )
    return out


def deserialize_json(data: dict) -> RerankResult:
    out: RerankResult = {}  # type: ignore[typeddict-item]
    if "index" in data:
        out["index"] = data["index"]
    else:
        raise DeserializationError("RerankResult.index required")
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        raise DeserializationError("RerankResult.relevance_score required")
    if "document" in data:
        import aws_sdk_bedrock_agent_runtime.types.rerank_document

        out["document"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_document.deserialize_json(
                data["document"]
            )
        )
    return out
