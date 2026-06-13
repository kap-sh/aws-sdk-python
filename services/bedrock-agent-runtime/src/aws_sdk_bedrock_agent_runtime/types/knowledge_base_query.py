"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.input_image
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type


class KnowledgeBaseQuery(TypedDict):
    type: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type.KnowledgeBaseQueryType"
    """<p>The type of query being performed.</p>"""
    text: "str"
    """<p>The text of the query made to the knowledge base.</p>"""
    image: NotRequired["aws_sdk_bedrock_agent_runtime.types.input_image.InputImage"]
    """<p>An image to include in the knowledge base query for multimodal retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseQuery) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type

    out["type"] = (
        aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type.serialize_json(
            value.get("type", "TEXT")
        )
    )
    out["text"] = value.get("text", "")
    if "image" in value:
        import aws_sdk_bedrock_agent_runtime.types.input_image

        out["image"] = aws_sdk_bedrock_agent_runtime.types.input_image.serialize_json(
            value["image"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseQuery:
    out: KnowledgeBaseQuery = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_query_type.deserialize_json(
                data["type"]
            )
        )
    else:
        out["type"] = "TEXT"
    if "text" in data:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if "image" in data:
        import aws_sdk_bedrock_agent_runtime.types.input_image

        out["image"] = aws_sdk_bedrock_agent_runtime.types.input_image.deserialize_json(
            data["image"]
        )
    return out
