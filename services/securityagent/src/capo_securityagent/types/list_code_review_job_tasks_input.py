"""Generated from Smithy shape ``com.amazonaws.securityagent#ListCodeReviewJobTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.step_name


class ListCodeReviewJobTasksInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job to list tasks for.</p>"""
    step_name: NotRequired["capo_securityagent.types.step_name.StepName"]
    """<p>Filter tasks by step name.</p>"""
    category_name: NotRequired["str"]
    """<p>Filter tasks by category name.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewJobTasksInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    if "step_name" in value:
        import capo_securityagent.types.step_name

        out["stepName"] = capo_securityagent.types.step_name.serialize_json(
            value["step_name"]
        )
    if "category_name" in value:
        out["categoryName"] = value["category_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeReviewJobTasksInput:
    out: ListCodeReviewJobTasksInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "ListCodeReviewJobTasksInput.agent_space_id required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if "stepName" in data:
        import capo_securityagent.types.step_name

        out["step_name"] = capo_securityagent.types.step_name.deserialize_json(
            data["stepName"]
        )
    if "categoryName" in data:
        out["category_name"] = data["categoryName"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
