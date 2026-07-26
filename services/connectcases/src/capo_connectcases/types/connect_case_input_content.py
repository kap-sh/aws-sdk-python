"""Generated from Smithy shape ``com.amazonaws.connectcases#ConnectCaseInputContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_id


class ConnectCaseInputContent(TypedDict, closed=True):
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectCaseInputContent) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> ConnectCaseInputContent:
    out: ConnectCaseInputContent = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("ConnectCaseInputContent.case_id required")
    return out
