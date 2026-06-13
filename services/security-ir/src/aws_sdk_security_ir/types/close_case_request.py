"""Generated from Smithy shape ``com.amazonaws.securityir#CloseCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id


class CloseCaseRequest(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element used in combination with CloseCase to identify the case ID to close.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloseCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CloseCaseRequest:
    out: CloseCaseRequest = {}  # type: ignore[typeddict-item]
    return out
