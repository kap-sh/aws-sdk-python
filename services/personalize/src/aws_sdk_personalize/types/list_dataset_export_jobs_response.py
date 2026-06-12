"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_export_jobs
    import aws_sdk_personalize.types.next_token


class ListDatasetExportJobsResponse(TypedDict):
    dataset_export_jobs: NotRequired[
        "aws_sdk_personalize.types.dataset_export_jobs.DatasetExportJobs"
    ]
    """<p>The list of dataset export jobs.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of dataset export jobs (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetExportJobsResponse) -> dict:
    out: dict = {}
    if "dataset_export_jobs" in value:
        import aws_sdk_personalize.types.dataset_export_jobs

        out["datasetExportJobs"] = (
            aws_sdk_personalize.types.dataset_export_jobs.serialize_aws_json_1_1(
                value["dataset_export_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetExportJobsResponse:
    out: ListDatasetExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "datasetExportJobs" in data:
        import aws_sdk_personalize.types.dataset_export_jobs

        out["dataset_export_jobs"] = (
            aws_sdk_personalize.types.dataset_export_jobs.deserialize_aws_json_1_1(
                data["datasetExportJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
