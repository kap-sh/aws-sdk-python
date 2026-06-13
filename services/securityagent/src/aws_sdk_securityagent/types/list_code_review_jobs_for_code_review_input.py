"""Generated from Smithy shape ``com.amazonaws.securityagent#ListCodeReviewJobsForCodeReviewInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token


class ListCodeReviewJobsForCodeReviewInput(TypedDict):
    max_results: NotRequired["aws_sdk_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    code_review_id: "str"
    """<p>The unique identifier of the code review to list jobs for.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewJobsForCodeReviewInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["codeReviewId"] = value["code_review_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeReviewJobsForCodeReviewInput:
    out: ListCodeReviewJobsForCodeReviewInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError(
            "ListCodeReviewJobsForCodeReviewInput.code_review_id required"
        )
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "ListCodeReviewJobsForCodeReviewInput.agent_space_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
