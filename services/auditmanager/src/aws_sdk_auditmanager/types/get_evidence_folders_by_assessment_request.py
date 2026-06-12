"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFoldersByAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.max_results
    import aws_sdk_auditmanager.types.token
    import aws_sdk_auditmanager.types.uuid


class GetEvidenceFoldersByAssessmentRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFoldersByAssessmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvidenceFoldersByAssessmentRequest:
    out: GetEvidenceFoldersByAssessmentRequest = {}  # type: ignore[typeddict-item]
    return out
