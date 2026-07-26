"""Generated from Smithy shape ``com.amazonaws.bedrock#ListEvaluationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_summaries
    import capo_bedrock.types.pagination_token


class ListEvaluationJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>"""
    job_summaries: NotRequired[
        "capo_bedrock.types.evaluation_summaries.EvaluationSummaries"
    ]
    """<p>A list of summaries of the evaluation jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "job_summaries" in value:
        import capo_bedrock.types.evaluation_summaries

        out["jobSummaries"] = capo_bedrock.types.evaluation_summaries.serialize_json(
            value["job_summaries"]
        )
    return out


def deserialize_json(data: dict) -> ListEvaluationJobsResponse:
    out: ListEvaluationJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "jobSummaries" in data:
        import capo_bedrock.types.evaluation_summaries

        out["job_summaries"] = capo_bedrock.types.evaluation_summaries.deserialize_json(
            data["jobSummaries"]
        )
    return out
