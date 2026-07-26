"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.framework


class CreateAssessmentFrameworkResponse(TypedDict, closed=True):
    framework: NotRequired["capo_auditmanager.types.framework.Framework"]
    """<p> The new framework object that the <code>CreateAssessmentFramework</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkResponse) -> dict:
    out: dict = {}
    if "framework" in value:
        import capo_auditmanager.types.framework

        out["framework"] = capo_auditmanager.types.framework.serialize_json(
            value["framework"]
        )
    return out


def deserialize_json(data: dict) -> CreateAssessmentFrameworkResponse:
    out: CreateAssessmentFrameworkResponse = {}  # type: ignore[typeddict-item]
    if "framework" in data:
        import capo_auditmanager.types.framework

        out["framework"] = capo_auditmanager.types.framework.deserialize_json(
            data["framework"]
        )
    return out
