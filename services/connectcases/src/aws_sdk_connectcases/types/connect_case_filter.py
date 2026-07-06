"""Generated from Smithy shape ``com.amazonaws.connectcases#ConnectCaseFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id


class ConnectCaseFilter(TypedDict, closed=True):
    case_id: NotRequired["aws_sdk_connectcases.types.case_id.CaseId"]
    """<p>A unique identifier of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectCaseFilter) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> ConnectCaseFilter:
    out: ConnectCaseFilter = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    return out
