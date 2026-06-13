"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievedReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata


class RetrievedReference(TypedDict):
    content: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content.RetrievalResultContent"
    ]
    """<p>Contains the cited text from the data source.</p>"""
    location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_location.RetrievalResultLocation"
    ]
    """<p>Contains information about the location of the data source.</p>"""
    metadata: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.RetrievalResultMetadata"
    ]
    """<p>Contains metadata attributes and their values for the file in the data source. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata\">Metadata and filtering</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedReference) -> dict:
    out: dict = {}
    if "content" in value:
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
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievedReference:
    out: RetrievedReference = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content.deserialize_json(
                data["content"]
            )
        )
    if "location" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_location.deserialize_json(
                data["location"]
            )
        )
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
