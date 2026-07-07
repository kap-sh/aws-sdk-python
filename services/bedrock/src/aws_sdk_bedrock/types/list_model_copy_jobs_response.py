"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelCopyJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_copy_job_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListModelCopyJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""
    model_copy_job_summaries: NotRequired[
        "aws_sdk_bedrock.types.model_copy_job_summaries.ModelCopyJobSummaries"
    ]
    """<p>A list of information about each model copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelCopyJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_copy_job_summaries" in value:
        import aws_sdk_bedrock.types.model_copy_job_summaries

        out["modelCopyJobSummaries"] = (
            aws_sdk_bedrock.types.model_copy_job_summaries.serialize_json(
                value["model_copy_job_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListModelCopyJobsResponse:
    out: ListModelCopyJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "modelCopyJobSummaries" in data:
        import aws_sdk_bedrock.types.model_copy_job_summaries

        out["model_copy_job_summaries"] = (
            aws_sdk_bedrock.types.model_copy_job_summaries.deserialize_json(
                data["modelCopyJobSummaries"]
            )
        )
    return out
