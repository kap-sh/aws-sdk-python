"""Generated from Smithy shape ``com.amazonaws.securityagent#StopCodeReviewJobInput``."""

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError


class StopCodeReviewJobInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    code_review_job_id: "str"
    """<p>The unique identifier of the code review job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCodeReviewJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["codeReviewJobId"] = value["code_review_job_id"]
    return out


def deserialize_json(data: dict) -> StopCodeReviewJobInput:
    out: StopCodeReviewJobInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("StopCodeReviewJobInput.agent_space_id required")
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    else:
        raise DeserializationError("StopCodeReviewJobInput.code_review_job_id required")
    return out
