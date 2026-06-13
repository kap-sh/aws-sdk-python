"""Generated from Smithy shape ``com.amazonaws.securityagent#ListCodeReviewsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token


class ListCodeReviewsInput(TypedDict):
    max_results: NotRequired["aws_sdk_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space to list code reviews for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> ListCodeReviewsInput:
    out: ListCodeReviewsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("ListCodeReviewsInput.agent_space_id required")
    return out
