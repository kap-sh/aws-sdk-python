"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment


class UpdateAssessmentResponse(TypedDict, closed=True):
    assessment: NotRequired["aws_sdk_auditmanager.types.assessment.Assessment"]
    """<p> The response object for the <code>UpdateAssessment</code> API. This is the name of the updated assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentResponse:
    out: UpdateAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out
