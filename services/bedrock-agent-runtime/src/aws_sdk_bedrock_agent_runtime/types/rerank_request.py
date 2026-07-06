"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.next_token
    import aws_sdk_bedrock_agent_runtime.types.rerank_queries_list
    import aws_sdk_bedrock_agent_runtime.types.rerank_sources_list
    import aws_sdk_bedrock_agent_runtime.types.reranking_configuration


class RerankRequest(TypedDict, closed=True):
    queries: "aws_sdk_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList"
    """<p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>"""
    sources: "aws_sdk_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList"
    """<p>An array of objects, each of which contains information about the sources to rerank.</p>"""
    reranking_configuration: "aws_sdk_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration"
    """<p>Contains configurations for reranking.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.rerank_queries_list

    out["queries"] = (
        aws_sdk_bedrock_agent_runtime.types.rerank_queries_list.serialize_json(
            value["queries"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.rerank_sources_list

    out["sources"] = (
        aws_sdk_bedrock_agent_runtime.types.rerank_sources_list.serialize_json(
            value["sources"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.reranking_configuration

    out["rerankingConfiguration"] = (
        aws_sdk_bedrock_agent_runtime.types.reranking_configuration.serialize_json(
            value["reranking_configuration"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RerankRequest:
    out: RerankRequest = {}  # type: ignore[typeddict-item]
    if "queries" in data:
        import aws_sdk_bedrock_agent_runtime.types.rerank_queries_list

        out["queries"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_queries_list.deserialize_json(
                data["queries"]
            )
        )
    else:
        raise DeserializationError("RerankRequest.queries required")
    if "sources" in data:
        import aws_sdk_bedrock_agent_runtime.types.rerank_sources_list

        out["sources"] = (
            aws_sdk_bedrock_agent_runtime.types.rerank_sources_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("RerankRequest.sources required")
    if "rerankingConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.reranking_configuration

        out["reranking_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    else:
        raise DeserializationError("RerankRequest.reranking_configuration required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
