"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentControlInsightsByControlDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment
    import aws_sdk_auditmanager.types.token


class ListAssessmentControlInsightsByControlDomainResponse(TypedDict, closed=True):
    control_insights_by_assessment: NotRequired[
        "aws_sdk_auditmanager.types.control_insights_metadata_by_assessment.ControlInsightsMetadataByAssessment"
    ]
    """<p>The assessment control analytics data that the <code>ListAssessmentControlInsightsByControlDomain</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentControlInsightsByControlDomainResponse) -> dict:
    out: dict = {}
    if "control_insights_by_assessment" in value:
        import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment

        out["controlInsightsByAssessment"] = (
            aws_sdk_auditmanager.types.control_insights_metadata_by_assessment.serialize_json(
                value["control_insights_by_assessment"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> ListAssessmentControlInsightsByControlDomainResponse:
    out: ListAssessmentControlInsightsByControlDomainResponse = {}  # type: ignore[typeddict-item]
    if "controlInsightsByAssessment" in data:
        import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment

        out["control_insights_by_assessment"] = (
            aws_sdk_auditmanager.types.control_insights_metadata_by_assessment.deserialize_json(
                data["controlInsightsByAssessment"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
