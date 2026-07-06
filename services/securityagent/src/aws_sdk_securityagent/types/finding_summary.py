"""Generated from Smithy shape ``com.amazonaws.securityagent#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.confidence_level
    import aws_sdk_securityagent.types.finding_status
    import aws_sdk_securityagent.types.risk_level


class FindingSummary(TypedDict, closed=True):
    finding_id: "str"
    """<p>The unique identifier of the finding.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space associated with the finding.</p>"""
    pentest_id: NotRequired["str"]
    """<p>The unique identifier of the pentest associated with the finding.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job that produced the finding.</p>"""
    code_review_id: NotRequired["str"]
    """<p>The unique identifier of the code review associated with the finding.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job that produced the finding.</p>"""
    name: NotRequired["str"]
    """<p>The name of the finding.</p>"""
    status: NotRequired["aws_sdk_securityagent.types.finding_status.FindingStatus"]
    """<p>The current status of the finding.</p>"""
    risk_type: NotRequired["str"]
    """<p>The type of security risk identified by the finding.</p>"""
    risk_level: NotRequired["aws_sdk_securityagent.types.risk_level.RiskLevel"]
    """<p>The risk level of the finding.</p>"""
    confidence: NotRequired[
        "aws_sdk_securityagent.types.confidence_level.ConfidenceLevel"
    ]
    """<p>The confidence level of the finding.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the finding was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the finding was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "pentest_id" in value:
        out["pentestId"] = value["pentest_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_id" in value:
        out["codeReviewId"] = value["code_review_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_securityagent.types.finding_status

        out["status"] = aws_sdk_securityagent.types.finding_status.serialize_json(
            value["status"]
        )
    if "risk_type" in value:
        out["riskType"] = value["risk_type"]
    if "risk_level" in value:
        import aws_sdk_securityagent.types.risk_level

        out["riskLevel"] = aws_sdk_securityagent.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "confidence" in value:
        import aws_sdk_securityagent.types.confidence_level

        out["confidence"] = aws_sdk_securityagent.types.confidence_level.serialize_json(
            value["confidence"]
        )
    if "created_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("FindingSummary.finding_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("FindingSummary.agent_space_id required")
    if "pentestId" in data:
        out["pentest_id"] = data["pentestId"]
    if "pentestJobId" in data:
        out["pentest_job_id"] = data["pentestJobId"]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_securityagent.types.finding_status

        out["status"] = aws_sdk_securityagent.types.finding_status.deserialize_json(
            data["status"]
        )
    if "riskType" in data:
        out["risk_type"] = data["riskType"]
    if "riskLevel" in data:
        import aws_sdk_securityagent.types.risk_level

        out["risk_level"] = aws_sdk_securityagent.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if "confidence" in data:
        import aws_sdk_securityagent.types.confidence_level

        out["confidence"] = (
            aws_sdk_securityagent.types.confidence_level.deserialize_json(
                data["confidence"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
