"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list
    import aws_sdk_bedrock_agentcore.types.memory_strategy_id
    import aws_sdk_bedrock_agentcore.types.sensitive_string


class SearchCriteria(TypedDict, closed=True):
    search_query: "aws_sdk_bedrock_agentcore.types.sensitive_string.SensitiveString"
    """<p>The search query to use for finding relevant memory records.</p>"""
    memory_strategy_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The memory strategy identifier to filter memory records by.</p>"""
    top_k: "int"
    """<p>The maximum number of top-scoring memory records to return. This value is used for semantic search ranking.</p>"""
    metadata_filters: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
    ]
    """<p>Filters to apply to metadata associated with a memory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCriteria) -> dict:
    out: dict = {}
    out["searchQuery"] = value["search_query"]
    if "memory_strategy_id" in value:
        out["memoryStrategyId"] = value["memory_strategy_id"]
    out["topK"] = value.get("top_k", 10)
    if "metadata_filters" in value:
        import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadataFilters"] = (
            aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list.serialize_json(
                value["metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchCriteria:
    out: SearchCriteria = {}  # type: ignore[typeddict-item]
    if "searchQuery" in data:
        out["search_query"] = data["searchQuery"]
    else:
        raise DeserializationError("SearchCriteria.search_query required")
    if "memoryStrategyId" in data:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    if "topK" in data:
        out["top_k"] = data["topK"]
    else:
        out["top_k"] = 10
    if "metadataFilters" in data:
        import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadata_filters"] = (
            aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list.deserialize_json(
                data["metadataFilters"]
            )
        )
    return out
