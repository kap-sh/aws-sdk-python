"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentFrameworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.framework


class GetAssessmentFrameworkResponse(TypedDict, closed=True):
    framework: NotRequired["aws_sdk_auditmanager.types.framework.Framework"]
    """<p> The framework that the <code>GetAssessmentFramework</code> API returned. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentFrameworkResponse) -> dict:
    out: dict = {}
    if "framework" in value:
        import aws_sdk_auditmanager.types.framework

        out["framework"] = aws_sdk_auditmanager.types.framework.serialize_json(
            value["framework"]
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentFrameworkResponse:
    out: GetAssessmentFrameworkResponse = {}  # type: ignore[typeddict-item]
    if "framework" in data:
        import aws_sdk_auditmanager.types.framework

        out["framework"] = aws_sdk_auditmanager.types.framework.deserialize_json(
            data["framework"]
        )
    return out
