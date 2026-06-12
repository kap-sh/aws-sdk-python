"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkShareResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_framework_share_request


class UpdateAssessmentFrameworkShareResponse(TypedDict):
    assessment_framework_share_request: NotRequired[
        "aws_sdk_auditmanager.types.assessment_framework_share_request.AssessmentFrameworkShareRequest"
    ]
    """<p> The updated share request that's returned by the <code>UpdateAssessmentFrameworkShare</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkShareResponse) -> dict:
    out: dict = {}
    if "assessment_framework_share_request" in value:
        import aws_sdk_auditmanager.types.assessment_framework_share_request

        out["assessmentFrameworkShareRequest"] = (
            aws_sdk_auditmanager.types.assessment_framework_share_request.serialize_json(
                value["assessment_framework_share_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkShareResponse:
    out: UpdateAssessmentFrameworkShareResponse = {}  # type: ignore[typeddict-item]
    if "assessmentFrameworkShareRequest" in data:
        import aws_sdk_auditmanager.types.assessment_framework_share_request

        out["assessment_framework_share_request"] = (
            aws_sdk_auditmanager.types.assessment_framework_share_request.deserialize_json(
                data["assessmentFrameworkShareRequest"]
            )
        )
    return out
