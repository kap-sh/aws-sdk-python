"""Generated from Smithy shape ``com.amazonaws.transfer#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token


class ListConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListConnectors</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional connectors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
