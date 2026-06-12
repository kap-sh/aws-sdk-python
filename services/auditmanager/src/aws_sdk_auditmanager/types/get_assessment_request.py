"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class GetAssessmentRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p>The unique identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssessmentRequest:
    out: GetAssessmentRequest = {}  # type: ignore[typeddict-item]
    return out
