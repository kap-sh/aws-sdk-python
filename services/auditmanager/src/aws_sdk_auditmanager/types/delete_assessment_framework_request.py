"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class DeleteAssessmentFrameworkRequest(TypedDict):
    framework_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the custom framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentFrameworkRequest:
    out: DeleteAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    return out
