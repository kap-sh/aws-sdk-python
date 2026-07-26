"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_job_id_list


class BatchGetCodeReviewJobsInput(TypedDict, closed=True):
    code_review_job_ids: (
        "capo_securityagent.types.code_review_job_id_list.CodeReviewJobIdList"
    )
    """<p>The list of code review job identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code review jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewJobsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.code_review_job_id_list

    out["codeReviewJobIds"] = (
        capo_securityagent.types.code_review_job_id_list.serialize_json(
            value["code_review_job_ids"]
        )
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewJobsInput:
    out: BatchGetCodeReviewJobsInput = {}  # type: ignore[typeddict-item]
    if "codeReviewJobIds" in data:
        import capo_securityagent.types.code_review_job_id_list

        out["code_review_job_ids"] = (
            capo_securityagent.types.code_review_job_id_list.deserialize_json(
                data["codeReviewJobIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCodeReviewJobsInput.code_review_job_ids required"
        )
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "BatchGetCodeReviewJobsInput.agent_space_id required"
        )
    return out
