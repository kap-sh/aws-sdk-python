"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetInsightsByAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class GetInsightsByAssessmentRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p>The unique identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightsByAssessmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInsightsByAssessmentRequest:
    out: GetInsightsByAssessmentRequest = {}  # type: ignore[typeddict-item]
    return out
