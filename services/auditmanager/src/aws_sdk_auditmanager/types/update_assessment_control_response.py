"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_control


class UpdateAssessmentControlResponse(TypedDict, closed=True):
    control: NotRequired[
        "aws_sdk_auditmanager.types.assessment_control.AssessmentControl"
    ]
    """<p> The name of the updated control set that the <code>UpdateAssessmentControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import aws_sdk_auditmanager.types.assessment_control

        out["control"] = aws_sdk_auditmanager.types.assessment_control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlResponse:
    out: UpdateAssessmentControlResponse = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import aws_sdk_auditmanager.types.assessment_control

        out["control"] = aws_sdk_auditmanager.types.assessment_control.deserialize_json(
            data["control"]
        )
    return out
