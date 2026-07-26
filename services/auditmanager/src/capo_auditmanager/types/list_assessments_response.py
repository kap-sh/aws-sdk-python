"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.list_assessment_metadata
    import capo_auditmanager.types.token


class ListAssessmentsResponse(TypedDict, closed=True):
    assessment_metadata: NotRequired[
        "capo_auditmanager.types.list_assessment_metadata.ListAssessmentMetadata"
    ]
    """<p>The metadata that the <code>ListAssessments</code> API returns for each assessment.</p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentsResponse) -> dict:
    out: dict = {}
    if "assessment_metadata" in value:
        import capo_auditmanager.types.list_assessment_metadata

        out["assessmentMetadata"] = (
            capo_auditmanager.types.list_assessment_metadata.serialize_json(
                value["assessment_metadata"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentsResponse:
    out: ListAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentMetadata" in data:
        import capo_auditmanager.types.list_assessment_metadata

        out["assessment_metadata"] = (
            capo_auditmanager.types.list_assessment_metadata.deserialize_json(
                data["assessmentMetadata"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
