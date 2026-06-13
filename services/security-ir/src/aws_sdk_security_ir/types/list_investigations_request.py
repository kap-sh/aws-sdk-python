"""Generated from Smithy shape ``com.amazonaws.securityir#ListInvestigationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id


class ListInvestigationsRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>Investigation performed by an agent for a security incident request</p>"""
    max_results: NotRequired["int"]
    """<p>Investigation performed by an agent for a security incident request, returning max results</p>"""
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Investigation performed by an agent for a security incident per caseID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInvestigationsRequest:
    out: ListInvestigationsRequest = {}  # type: ignore[typeddict-item]
    return out
