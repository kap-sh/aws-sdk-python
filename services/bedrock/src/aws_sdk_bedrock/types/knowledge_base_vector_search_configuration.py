"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseVectorSearchConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.implicit_filter_configuration
    import aws_sdk_bedrock.types.retrieval_filter
    import aws_sdk_bedrock.types.search_type
    import aws_sdk_bedrock.types.vector_search_reranking_configuration


class KnowledgeBaseVectorSearchConfiguration(TypedDict):
    number_of_results: NotRequired["int"]
    """<p>The number of text chunks to retrieve; the number of results to return.</p>"""
    override_search_type: NotRequired["aws_sdk_bedrock.types.search_type.SearchType"]
    """<p>By default, Amazon Bedrock decides a search strategy for you. If you're using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a <code>HYBRID</code> search using both vector embeddings and raw text, or <code>SEMANTIC</code> search using only vector embeddings. For other vector store configurations, only <code>SEMANTIC</code> search is available.</p>"""
    filter: NotRequired["aws_sdk_bedrock.types.retrieval_filter.RetrievalFilter"]
    """<p>Specifies the filters to use on the metadata fields in the knowledge base data sources before returning results.</p>"""
    implicit_filter_configuration: NotRequired[
        "aws_sdk_bedrock.types.implicit_filter_configuration.ImplicitFilterConfiguration"
    ]
    """<p>Configuration for implicit filtering in Knowledge Base vector searches. This allows the system to automatically apply filters based on the query context without requiring explicit filter expressions.</p>"""
    reranking_configuration: NotRequired[
        "aws_sdk_bedrock.types.vector_search_reranking_configuration.VectorSearchRerankingConfiguration"
    ]
    """<p>Configuration for reranking search results in Knowledge Base vector searches. Reranking improves search relevance by reordering initial vector search results using more sophisticated relevance models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseVectorSearchConfiguration) -> dict:
    out: dict = {}
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    if "override_search_type" in value:
        import aws_sdk_bedrock.types.search_type

        out["overrideSearchType"] = aws_sdk_bedrock.types.search_type.serialize_json(
            value["override_search_type"]
        )
    if "filter" in value:
        import aws_sdk_bedrock.types.retrieval_filter

        out["filter"] = aws_sdk_bedrock.types.retrieval_filter.serialize_json(
            value["filter"]
        )
    if "implicit_filter_configuration" in value:
        import aws_sdk_bedrock.types.implicit_filter_configuration

        out["implicitFilterConfiguration"] = (
            aws_sdk_bedrock.types.implicit_filter_configuration.serialize_json(
                value["implicit_filter_configuration"]
            )
        )
    if "reranking_configuration" in value:
        import aws_sdk_bedrock.types.vector_search_reranking_configuration

        out["rerankingConfiguration"] = (
            aws_sdk_bedrock.types.vector_search_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseVectorSearchConfiguration:
    out: KnowledgeBaseVectorSearchConfiguration = {}  # type: ignore[typeddict-item]
    if "numberOfResults" in data:
        out["number_of_results"] = data["numberOfResults"]
    if "overrideSearchType" in data:
        import aws_sdk_bedrock.types.search_type

        out["override_search_type"] = (
            aws_sdk_bedrock.types.search_type.deserialize_json(
                data["overrideSearchType"]
            )
        )
    if "filter" in data:
        import aws_sdk_bedrock.types.retrieval_filter

        out["filter"] = aws_sdk_bedrock.types.retrieval_filter.deserialize_json(
            data["filter"]
        )
    if "implicitFilterConfiguration" in data:
        import aws_sdk_bedrock.types.implicit_filter_configuration

        out["implicit_filter_configuration"] = (
            aws_sdk_bedrock.types.implicit_filter_configuration.deserialize_json(
                data["implicitFilterConfiguration"]
            )
        )
    if "rerankingConfiguration" in data:
        import aws_sdk_bedrock.types.vector_search_reranking_configuration

        out["reranking_configuration"] = (
            aws_sdk_bedrock.types.vector_search_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    return out
