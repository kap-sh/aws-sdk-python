"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.dataset_import_jobs
    import capo_personalize.types.next_token


class ListDatasetImportJobsResponse(TypedDict, closed=True):
    dataset_import_jobs: NotRequired[
        "capo_personalize.types.dataset_import_jobs.DatasetImportJobs"
    ]
    """<p>The list of dataset import jobs.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of dataset import jobs (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetImportJobsResponse) -> dict:
    out: dict = {}
    if "dataset_import_jobs" in value:
        import capo_personalize.types.dataset_import_jobs

        out["datasetImportJobs"] = (
            capo_personalize.types.dataset_import_jobs.serialize_aws_json_1_1(
                value["dataset_import_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetImportJobsResponse:
    out: ListDatasetImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "datasetImportJobs" in data:
        import capo_personalize.types.dataset_import_jobs

        out["dataset_import_jobs"] = (
            capo_personalize.types.dataset_import_jobs.deserialize_aws_json_1_1(
                data["datasetImportJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
