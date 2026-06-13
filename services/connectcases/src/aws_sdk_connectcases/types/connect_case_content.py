"""Generated from Smithy shape ``com.amazonaws.connectcases#ConnectCaseContent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id


class ConnectCaseContent(TypedDict):
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectCaseContent) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> ConnectCaseContent:
    out: ConnectCaseContent = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("ConnectCaseContent.case_id required")
    return out
