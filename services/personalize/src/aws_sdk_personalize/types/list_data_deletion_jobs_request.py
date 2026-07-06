"""Generated from Smithy shape ``com.amazonaws.personalize#ListDataDeletionJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.max_results
    import aws_sdk_personalize.types.next_token


class ListDataDeletionJobsRequest(TypedDict, closed=True):
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group to list data deletion jobs for.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListDataDeletionJobs</code> for getting the next set of jobs (if they exist).</p>"""
    max_results: NotRequired["aws_sdk_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of data deletion jobs to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataDeletionJobsRequest) -> dict:
    out: dict = {}
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataDeletionJobsRequest:
    out: ListDataDeletionJobsRequest = {}  # type: ignore[typeddict-item]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
