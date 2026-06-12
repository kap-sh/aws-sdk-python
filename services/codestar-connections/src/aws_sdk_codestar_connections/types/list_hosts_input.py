"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListHostsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.max_results
    import aws_sdk_codestar_connections.types.next_token


class ListHostsInput(TypedDict):
    max_results: "aws_sdk_codestar_connections.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_codestar_connections.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListHosts</code> call, which can be used to return the next set of hosts in the list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListHostsInput) -> dict:
    out: dict = {}
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListHostsInput:
    out: ListHostsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
