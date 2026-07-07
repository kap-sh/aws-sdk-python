"""Generated from Smithy shape ``com.amazonaws.forecast#ListDatasetGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.max_results
    import aws_sdk_forecast.types.next_token


class ListDatasetGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""
    max_results: NotRequired["aws_sdk_forecast.types.max_results.MaxResults"]
    """<p>The number of items to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetGroupsRequest:
    out: ListDatasetGroupsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
