"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListIngestionJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.ingestion_job_filters
    import capo_bedrock_agent.types.ingestion_job_sort_by
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token


class ListIngestionJobsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the list of data ingestion jobs.</p>"""
    filters: NotRequired[
        "capo_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
    ]
    """<p>Contains information about the filters for filtering the data.</p>"""
    sort_by: NotRequired[
        "capo_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
    ]
    """<p>Contains details about how to sort the data.</p>"""
    max_results: NotRequired["capo_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionJobsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_bedrock_agent.types.ingestion_job_filters

        out["filters"] = capo_bedrock_agent.types.ingestion_job_filters.serialize_json(
            value["filters"]
        )
    if "sort_by" in value:
        import capo_bedrock_agent.types.ingestion_job_sort_by

        out["sortBy"] = capo_bedrock_agent.types.ingestion_job_sort_by.serialize_json(
            value["sort_by"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIngestionJobsRequest:
    out: ListIngestionJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_bedrock_agent.types.ingestion_job_filters

        out["filters"] = (
            capo_bedrock_agent.types.ingestion_job_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_bedrock_agent.types.ingestion_job_sort_by

        out["sort_by"] = (
            capo_bedrock_agent.types.ingestion_job_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
