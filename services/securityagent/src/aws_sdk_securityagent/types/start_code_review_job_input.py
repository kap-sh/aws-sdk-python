"""Generated from Smithy shape ``com.amazonaws.securityagent#StartCodeReviewJobInput``."""

from typing import TypedDict

from aws_sdk_securityagent.errors import DeserializationError


class StartCodeReviewJobInput(TypedDict):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    code_review_id: "str"
    """<p>The unique identifier of the code review to start a job for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeReviewJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["codeReviewId"] = value["code_review_id"]
    return out


def deserialize_json(data: dict) -> StartCodeReviewJobInput:
    out: StartCodeReviewJobInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("StartCodeReviewJobInput.agent_space_id required")
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("StartCodeReviewJobInput.code_review_id required")
    return out
