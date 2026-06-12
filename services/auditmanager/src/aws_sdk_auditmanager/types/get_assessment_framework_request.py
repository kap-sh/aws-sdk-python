"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class GetAssessmentFrameworkRequest(TypedDict):
    framework_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssessmentFrameworkRequest:
    out: GetAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    return out
