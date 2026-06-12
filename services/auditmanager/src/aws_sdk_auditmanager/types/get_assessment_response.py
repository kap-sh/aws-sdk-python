"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment
    import aws_sdk_auditmanager.types.role


class GetAssessmentResponse(TypedDict):
    assessment: NotRequired["aws_sdk_auditmanager.types.assessment.Assessment"]
    user_role: NotRequired["aws_sdk_auditmanager.types.role.Role"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    if "user_role" in value:
        import aws_sdk_auditmanager.types.role

        out["userRole"] = aws_sdk_auditmanager.types.role.serialize_json(
            value["user_role"]
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentResponse:
    out: GetAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import aws_sdk_auditmanager.types.assessment

        out["assessment"] = aws_sdk_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    if "userRole" in data:
        import aws_sdk_auditmanager.types.role

        out["user_role"] = aws_sdk_auditmanager.types.role.deserialize_json(
            data["userRole"]
        )
    return out
