"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_import_job_summaries
    import capo_bedrock.types.pagination_token


class ListModelImportJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    model_import_job_summaries: NotRequired[
        "capo_bedrock.types.model_import_job_summaries.ModelImportJobSummaries"
    ]
    """<p>Import job summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelImportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_import_job_summaries" in value:
        import capo_bedrock.types.model_import_job_summaries

        out["modelImportJobSummaries"] = (
            capo_bedrock.types.model_import_job_summaries.serialize_json(
                value["model_import_job_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListModelImportJobsResponse:
    out: ListModelImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("modelImportJobSummaries") is not None:
        import capo_bedrock.types.model_import_job_summaries

        out["model_import_job_summaries"] = (
            capo_bedrock.types.model_import_job_summaries.deserialize_json(
                data["modelImportJobSummaries"]
            )
        )
    return out
