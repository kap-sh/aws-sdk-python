"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.list_channels_max_results_count
    import capo_cloudtrail.types.pagination_token


class ListChannelsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_cloudtrail.types.list_channels_max_results_count.ListChannelsMaxResultsCount"
    ]
    """<p> The maximum number of CloudTrail channels to display on a single page. </p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChannelsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
