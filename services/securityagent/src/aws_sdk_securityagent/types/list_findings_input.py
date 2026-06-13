"""Generated from Smithy shape ``com.amazonaws.securityagent#ListFindingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.confidence_level
    import aws_sdk_securityagent.types.finding_status
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token
    import aws_sdk_securityagent.types.risk_level


class ListFindingsInput(TypedDict):
    max_results: NotRequired["aws_sdk_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job to list findings for.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job to list findings for. Mutually exclusive with pentestJobId.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""
    risk_type: NotRequired["str"]
    """<p>Filter findings by risk type.</p>"""
    risk_level: NotRequired["aws_sdk_securityagent.types.risk_level.RiskLevel"]
    """<p>Filter findings by risk level.</p>"""
    status: NotRequired["aws_sdk_securityagent.types.finding_status.FindingStatus"]
    """<p>Filter findings by status.</p>"""
    confidence: NotRequired[
        "aws_sdk_securityagent.types.confidence_level.ConfidenceLevel"
    ]
    """<p>Filter findings by confidence level.</p>"""
    name: NotRequired["str"]
    """<p>Filter findings by name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "risk_type" in value:
        out["riskType"] = value["risk_type"]
    if "risk_level" in value:
        import aws_sdk_securityagent.types.risk_level

        out["riskLevel"] = aws_sdk_securityagent.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "status" in value:
        import aws_sdk_securityagent.types.finding_status

        out["status"] = aws_sdk_securityagent.types.finding_status.serialize_json(
            value["status"]
        )
    if "confidence" in value:
        import aws_sdk_securityagent.types.confidence_level

        out["confidence"] = aws_sdk_securityagent.types.confidence_level.serialize_json(
            value["confidence"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListFindingsInput:
    out: ListFindingsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "pentestJobId" in data:
        out["pentest_job_id"] = data["pentestJobId"]
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("ListFindingsInput.agent_space_id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "riskType" in data:
        out["risk_type"] = data["riskType"]
    if "riskLevel" in data:
        import aws_sdk_securityagent.types.risk_level

        out["risk_level"] = aws_sdk_securityagent.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if "status" in data:
        import aws_sdk_securityagent.types.finding_status

        out["status"] = aws_sdk_securityagent.types.finding_status.deserialize_json(
            data["status"]
        )
    if "confidence" in data:
        import aws_sdk_securityagent.types.confidence_level

        out["confidence"] = (
            aws_sdk_securityagent.types.confidence_level.deserialize_json(
                data["confidence"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
