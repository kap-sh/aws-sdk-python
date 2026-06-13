"""Generated from Smithy shape ``com.amazonaws.securityagent#ListTargetDomainsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token


class ListTargetDomainsInput(TypedDict):
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""
    max_results: NotRequired["aws_sdk_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetDomainsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTargetDomainsInput:
    out: ListTargetDomainsInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
