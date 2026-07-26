"""Generated from Smithy shape ``com.amazonaws.securityir#CloseCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.case_status


class CloseCaseResponse(TypedDict, closed=True):
    case_status: NotRequired["capo_security_ir.types.case_status.CaseStatus"]
    """<p>A response element providing responses for requests to CloseCase. This element responds <code>Closed </code> if successful. </p>"""
    closed_date: NotRequired["datetime.datetime"]
    """<p>A response element providing responses for requests to CloseCase. This element responds with the ISO-8601 formatted timestamp of the moment when the case was closed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloseCaseResponse) -> dict:
    out: dict = {}
    if "case_status" in value:
        import capo_security_ir.types.case_status

        out["caseStatus"] = capo_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "closed_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["closedDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["closed_date"]
        )
    return out


def deserialize_json(data: dict) -> CloseCaseResponse:
    out: CloseCaseResponse = {}  # type: ignore[typeddict-item]
    if "caseStatus" in data:
        import capo_security_ir.types.case_status

        out["case_status"] = capo_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if "closedDate" in data:
        import capo_security_ir.types._prelude.timestamp

        out["closed_date"] = capo_security_ir.types._prelude.timestamp.deserialize_json(
            data["closedDate"]
        )
    return out
