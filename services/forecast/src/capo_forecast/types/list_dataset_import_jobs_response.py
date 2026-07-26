"""Generated from Smithy shape ``com.amazonaws.forecast#ListDatasetImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.dataset_import_jobs
    import capo_forecast.types.next_token


class ListDatasetImportJobsResponse(TypedDict, closed=True):
    dataset_import_jobs: NotRequired[
        "capo_forecast.types.dataset_import_jobs.DatasetImportJobs"
    ]
    """<p>An array of objects that summarize each dataset import job's properties.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetImportJobsResponse) -> dict:
    out: dict = {}
    if "dataset_import_jobs" in value:
        import capo_forecast.types.dataset_import_jobs

        out["DatasetImportJobs"] = (
            capo_forecast.types.dataset_import_jobs.serialize_aws_json_1_1(
                value["dataset_import_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetImportJobsResponse:
    out: ListDatasetImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "DatasetImportJobs" in data:
        import capo_forecast.types.dataset_import_jobs

        out["dataset_import_jobs"] = (
            capo_forecast.types.dataset_import_jobs.deserialize_aws_json_1_1(
                data["DatasetImportJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
