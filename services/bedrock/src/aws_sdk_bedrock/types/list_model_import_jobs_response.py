"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_import_job_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListModelImportJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    model_import_job_summaries: NotRequired[
        "aws_sdk_bedrock.types.model_import_job_summaries.ModelImportJobSummaries"
    ]
    """<p>Import job summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelImportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_import_job_summaries" in value:
        import aws_sdk_bedrock.types.model_import_job_summaries

        out["modelImportJobSummaries"] = (
            aws_sdk_bedrock.types.model_import_job_summaries.serialize_json(
                value["model_import_job_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListModelImportJobsResponse:
    out: ListModelImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "modelImportJobSummaries" in data:
        import aws_sdk_bedrock.types.model_import_job_summaries

        out["model_import_job_summaries"] = (
            aws_sdk_bedrock.types.model_import_job_summaries.deserialize_json(
                data["modelImportJobSummaries"]
            )
        )
    return out
