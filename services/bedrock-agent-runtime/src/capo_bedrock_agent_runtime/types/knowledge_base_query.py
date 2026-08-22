"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.input_image
    import capo_bedrock_agent_runtime.types.knowledge_base_query_type


class KnowledgeBaseQuery(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.knowledge_base_query_type.KnowledgeBaseQueryType"
    """<p>The type of query being performed.</p>"""
    text: "str"
    """<p>The text of the query made to the knowledge base.</p>"""
    image: NotRequired["capo_bedrock_agent_runtime.types.input_image.InputImage"]
    """<p>An image to include in the knowledge base query for multimodal retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseQuery) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.knowledge_base_query_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.knowledge_base_query_type.serialize_json(
            value.get("type", "TEXT")
        )
    )
    out["text"] = value.get("text", "")
    if "image" in value:
        import capo_bedrock_agent_runtime.types.input_image

        out["image"] = capo_bedrock_agent_runtime.types.input_image.serialize_json(
            value["image"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseQuery:
    out: KnowledgeBaseQuery = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_query_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_query_type.deserialize_json(
                data["type"]
            )
        )
    else:
        out["type"] = "TEXT"
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("image") is not None:
        import capo_bedrock_agent_runtime.types.input_image

        out["image"] = capo_bedrock_agent_runtime.types.input_image.deserialize_json(
            data["image"]
        )
    return out
