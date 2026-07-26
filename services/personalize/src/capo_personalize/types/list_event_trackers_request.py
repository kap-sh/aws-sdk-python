"""Generated from Smithy shape ``com.amazonaws.personalize#ListEventTrackersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListEventTrackersRequest(TypedDict, closed=True):
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of a dataset group used to filter the response.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListEventTrackers</code> for getting the next set of event trackers (if they exist).</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of event trackers to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventTrackersRequest) -> dict:
    out: dict = {}
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventTrackersRequest:
    out: ListEventTrackersRequest = {}  # type: ignore[typeddict-item]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
