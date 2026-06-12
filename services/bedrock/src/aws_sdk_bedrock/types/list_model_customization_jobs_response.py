"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelCustomizationJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_customization_job_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListModelCustomizationJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""
    model_customization_job_summaries: NotRequired[
        "aws_sdk_bedrock.types.model_customization_job_summaries.ModelCustomizationJobSummaries"
    ]
    """<p>Job summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelCustomizationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_customization_job_summaries" in value:
        import aws_sdk_bedrock.types.model_customization_job_summaries

        out["modelCustomizationJobSummaries"] = (
            aws_sdk_bedrock.types.model_customization_job_summaries.serialize_json(
                value["model_customization_job_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListModelCustomizationJobsResponse:
    out: ListModelCustomizationJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "modelCustomizationJobSummaries" in data:
        import aws_sdk_bedrock.types.model_customization_job_summaries

        out["model_customization_job_summaries"] = (
            aws_sdk_bedrock.types.model_customization_job_summaries.deserialize_json(
                data["modelCustomizationJobSummaries"]
            )
        )
    return out
