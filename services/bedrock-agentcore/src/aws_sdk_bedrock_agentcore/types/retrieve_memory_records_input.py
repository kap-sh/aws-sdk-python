"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RetrieveMemoryRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.namespace
    import aws_sdk_bedrock_agentcore.types.pagination_token
    import aws_sdk_bedrock_agentcore.types.search_criteria


class RetrieveMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>"""
    namespace: NotRequired["aws_sdk_bedrock_agentcore.types.namespace.Namespace"]
    """<p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>"""
    namespace_path: NotRequired["aws_sdk_bedrock_agentcore.types.namespace.Namespace"]
    """<p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>"""
    search_criteria: "aws_sdk_bedrock_agentcore.types.search_criteria.SearchCriteria"
    """<p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: "aws_sdk_bedrock_agentcore.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveMemoryRecordsInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "namespace_path" in value:
        out["namespacePath"] = value["namespace_path"]
    import aws_sdk_bedrock_agentcore.types.search_criteria

    out["searchCriteria"] = (
        aws_sdk_bedrock_agentcore.types.search_criteria.serialize_json(
            value["search_criteria"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 100)
    return out


def deserialize_json(data: dict) -> RetrieveMemoryRecordsInput:
    out: RetrieveMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "namespacePath" in data:
        out["namespace_path"] = data["namespacePath"]
    if "searchCriteria" in data:
        import aws_sdk_bedrock_agentcore.types.search_criteria

        out["search_criteria"] = (
            aws_sdk_bedrock_agentcore.types.search_criteria.deserialize_json(
                data["searchCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "RetrieveMemoryRecordsInput.search_criteria required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    return out
