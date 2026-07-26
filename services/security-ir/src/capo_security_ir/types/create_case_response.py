"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.case_id


class CreateCaseResponse(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>A response element providing responses for requests to CreateCase. This element responds with the case ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> CreateCaseResponse:
    out: CreateCaseResponse = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("CreateCaseResponse.case_id required")
    return out
