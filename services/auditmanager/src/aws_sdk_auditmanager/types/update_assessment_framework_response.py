"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.framework


class UpdateAssessmentFrameworkResponse(TypedDict):
    framework: NotRequired["aws_sdk_auditmanager.types.framework.Framework"]
    """<p> The framework object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkResponse) -> dict:
    out: dict = {}
    if "framework" in value:
        import aws_sdk_auditmanager.types.framework

        out["framework"] = aws_sdk_auditmanager.types.framework.serialize_json(
            value["framework"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkResponse:
    out: UpdateAssessmentFrameworkResponse = {}  # type: ignore[typeddict-item]
    if "framework" in data:
        import aws_sdk_auditmanager.types.framework

        out["framework"] = aws_sdk_auditmanager.types.framework.deserialize_json(
            data["framework"]
        )
    return out
