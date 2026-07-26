"""Generated from Smithy shape ``com.amazonaws.personalize#ListBatchInferenceJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListBatchInferenceJobsRequest(TypedDict, closed=True):
    solution_version_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution version from which the batch inference jobs were created.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of batch inference job results to return in each page. The default value is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBatchInferenceJobsRequest) -> dict:
    out: dict = {}
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBatchInferenceJobsRequest:
    out: ListBatchInferenceJobsRequest = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
