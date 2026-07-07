"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentFrameworkShareRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_framework_share_request_list
    import aws_sdk_auditmanager.types.token


class ListAssessmentFrameworkShareRequestsResponse(TypedDict, closed=True):
    assessment_framework_share_requests: NotRequired[
        "aws_sdk_auditmanager.types.assessment_framework_share_request_list.AssessmentFrameworkShareRequestList"
    ]
    """<p> The list of share requests that the <code>ListAssessmentFrameworkShareRequests</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentFrameworkShareRequestsResponse) -> dict:
    out: dict = {}
    if "assessment_framework_share_requests" in value:
        import aws_sdk_auditmanager.types.assessment_framework_share_request_list

        out["assessmentFrameworkShareRequests"] = (
            aws_sdk_auditmanager.types.assessment_framework_share_request_list.serialize_json(
                value["assessment_framework_share_requests"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentFrameworkShareRequestsResponse:
    out: ListAssessmentFrameworkShareRequestsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentFrameworkShareRequests" in data:
        import aws_sdk_auditmanager.types.assessment_framework_share_request_list

        out["assessment_framework_share_requests"] = (
            aws_sdk_auditmanager.types.assessment_framework_share_request_list.deserialize_json(
                data["assessmentFrameworkShareRequests"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
