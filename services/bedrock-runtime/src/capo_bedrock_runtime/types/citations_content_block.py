"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationsContentBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citation_generated_content_list
    import capo_bedrock_runtime.types.citations


class CitationsContentBlock(TypedDict, closed=True):
    content: NotRequired[
        "capo_bedrock_runtime.types.citation_generated_content_list.CitationGeneratedContentList"
    ]
    """<p>The generated content that is supported by the associated citations.</p>"""
    citations: NotRequired["capo_bedrock_runtime.types.citations.Citations"]
    """<p>An array of citations that reference the source documents used to generate the associated content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationsContentBlock) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_bedrock_runtime.types.citation_generated_content_list

        out["content"] = (
            capo_bedrock_runtime.types.citation_generated_content_list.serialize_json(
                value["content"]
            )
        )
    if "citations" in value:
        import capo_bedrock_runtime.types.citations

        out["citations"] = capo_bedrock_runtime.types.citations.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> CitationsContentBlock:
    out: CitationsContentBlock = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.citation_generated_content_list

        out["content"] = (
            capo_bedrock_runtime.types.citation_generated_content_list.deserialize_json(
                data["content"]
            )
        )
    if data.get("citations") is not None:
        import capo_bedrock_runtime.types.citations

        out["citations"] = capo_bedrock_runtime.types.citations.deserialize_json(
            data["citations"]
        )
    return out
