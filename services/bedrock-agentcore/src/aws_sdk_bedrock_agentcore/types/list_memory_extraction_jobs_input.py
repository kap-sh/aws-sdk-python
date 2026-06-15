"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryExtractionJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.extraction_job_filter_input
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListMemoryExtractionJobsInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory to list extraction jobs for.</p>"""
    max_results: "int"
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    filter: NotRequired[
        "aws_sdk_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
    ]
    """<p>Filter criteria to apply when listing extraction jobs.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryExtractionJobsInput) -> dict:
    out: dict = {}
    out["maxResults"] = value.get("max_results", 20)
    if "filter" in value:
        import aws_sdk_bedrock_agentcore.types.extraction_job_filter_input

        out["filter"] = (
            aws_sdk_bedrock_agentcore.types.extraction_job_filter_input.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryExtractionJobsInput:
    out: ListMemoryExtractionJobsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 20
    if "filter" in data:
        import aws_sdk_bedrock_agentcore.types.extraction_job_filter_input

        out["filter"] = (
            aws_sdk_bedrock_agentcore.types.extraction_job_filter_input.deserialize_json(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
