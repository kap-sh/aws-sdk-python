"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id


class GetCaseRequest(TypedDict, closed=True):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element for GetCase to identify the requested case ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCaseRequest:
    out: GetCaseRequest = {}  # type: ignore[typeddict-item]
    return out
