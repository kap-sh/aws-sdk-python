"""Generated from Smithy shape ``com.amazonaws.securityagent#StartCodeReviewJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.job_status


class StartCodeReviewJobOutput(TypedDict, closed=True):
    title: NotRequired["str"]
    """<p>The title of the code review job.</p>"""
    status: NotRequired["capo_securityagent.types.job_status.JobStatus"]
    """<p>The current status of the code review job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was last updated, in UTC format.</p>"""
    code_review_id: "str"
    """<p>The unique identifier of the code review.</p>"""
    code_review_job_id: "str"
    """<p>The unique identifier of the started code review job.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeReviewJobOutput) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "status" in value:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    out["codeReviewId"] = value["code_review_id"]
    out["codeReviewJobId"] = value["code_review_job_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> StartCodeReviewJobOutput:
    out: StartCodeReviewJobOutput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "status" in data:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("StartCodeReviewJobOutput.code_review_id required")
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    else:
        raise DeserializationError(
            "StartCodeReviewJobOutput.code_review_job_id required"
        )
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    return out
