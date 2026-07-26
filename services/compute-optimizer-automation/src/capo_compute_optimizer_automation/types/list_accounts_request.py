"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.next_token


class ListAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p> The maximum number of results to return in a single call. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token for the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountsRequest:
    out: ListAccountsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
