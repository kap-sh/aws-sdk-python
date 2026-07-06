"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrievalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata


class KnowledgeBaseRetrievalResult(TypedDict, closed=True):
    content: "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content.RetrievalResultContent"
    """<p>Contains information about the content of the chunk.</p>"""
    location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_location.RetrievalResultLocation"
    ]
    """<p>Contains information about the location of the data source.</p>"""
    score: NotRequired["float"]
    """<p>The level of relevance of the result to the query.</p>"""
    metadata: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.RetrievalResultMetadata"
    ]
    r"""<p>Contains metadata attributes and their values for the file in the data source. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata\">Metadata and filtering</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalResult) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.retrieval_result_content.serialize_json(
            value["content"]
        )
    )
    if "location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_location.serialize_json(
                value["location"]
            )
        )
    if "score" in value:
        out["score"] = value["score"]
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalResult:
    out: KnowledgeBaseRetrievalResult = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseRetrievalResult.content required")
    if "location" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_location.deserialize_json(
                data["location"]
            )
        )
    if "score" in data:
        out["score"] = data["score"]
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
