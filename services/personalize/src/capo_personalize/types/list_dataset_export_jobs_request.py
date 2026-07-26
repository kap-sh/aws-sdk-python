"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListDatasetExportJobsRequest(TypedDict, closed=True):
    dataset_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset to list the dataset export jobs for.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListDatasetExportJobs</code> for getting the next set of dataset export jobs (if they exist).</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of dataset export jobs to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetExportJobsRequest) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetExportJobsRequest:
    out: ListDatasetExportJobsRequest = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
