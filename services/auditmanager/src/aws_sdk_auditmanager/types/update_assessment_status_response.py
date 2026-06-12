"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment


class UpdateAssessmentStatusResponse(TypedDict):
    assessment: NotRequired["aws_sdk_auditmanager.types.assessment.Assessment"]
    """<p> The name of the updated assessment that the <code>UpdateAssessmentStatus</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentStatusResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentStatusResponse:
    out: UpdateAssessmentStatusResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out
