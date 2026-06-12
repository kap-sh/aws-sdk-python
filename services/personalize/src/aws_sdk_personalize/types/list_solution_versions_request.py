"""Generated from Smithy shape ``com.amazonaws.personalize#ListSolutionVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.max_results
    import aws_sdk_personalize.types.next_token


class ListSolutionVersionsRequest(TypedDict):
    solution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListSolutionVersions</code> for getting the next set of solution versions (if they exist).</p>"""
    max_results: NotRequired["aws_sdk_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of solution versions to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSolutionVersionsRequest) -> dict:
    out: dict = {}
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSolutionVersionsRequest:
    out: ListSolutionVersionsRequest = {}  # type: ignore[typeddict-item]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
