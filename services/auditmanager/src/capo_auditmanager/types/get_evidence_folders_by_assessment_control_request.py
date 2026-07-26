"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFoldersByAssessmentControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.token
    import capo_auditmanager.types.uuid


class GetEvidenceFoldersByAssessmentControlRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId"
    """<p> The identifier for the control set. </p>"""
    control_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["capo_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFoldersByAssessmentControlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvidenceFoldersByAssessmentControlRequest:
    out: GetEvidenceFoldersByAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    return out
