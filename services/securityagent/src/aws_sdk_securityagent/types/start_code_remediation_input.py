"""Generated from Smithy shape ``com.amazonaws.securityagent#StartCodeRemediationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.finding_id_list


class StartCodeRemediationInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job that produced the findings. Mutually exclusive with <code>codeReviewJobId</code>.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job that produced the findings. Mutually exclusive with <code>pentestJobId</code>.</p>"""
    finding_ids: "aws_sdk_securityagent.types.finding_id_list.FindingIdList"
    """<p>The list of finding identifiers to initiate code remediation for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeRemediationInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    import aws_sdk_securityagent.types.finding_id_list

    out["findingIds"] = aws_sdk_securityagent.types.finding_id_list.serialize_json(
        value["finding_ids"]
    )
    return out


def deserialize_json(data: dict) -> StartCodeRemediationInput:
    out: StartCodeRemediationInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("StartCodeRemediationInput.agent_space_id required")
    if "pentestJobId" in data:
        out["pentest_job_id"] = data["pentestJobId"]
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if "findingIds" in data:
        import aws_sdk_securityagent.types.finding_id_list

        out["finding_ids"] = (
            aws_sdk_securityagent.types.finding_id_list.deserialize_json(
                data["findingIds"]
            )
        )
    else:
        raise DeserializationError("StartCodeRemediationInput.finding_ids required")
    return out
