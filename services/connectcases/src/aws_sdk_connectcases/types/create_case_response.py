"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_arn
    import aws_sdk_connectcases.types.case_id


class CreateCaseResponse(TypedDict):
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    case_arn: "aws_sdk_connectcases.types.case_arn.CaseArn"
    """<p>The Amazon Resource Name (ARN) of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    out["caseArn"] = value["case_arn"]
    return out


def deserialize_json(data: dict) -> CreateCaseResponse:
    out: CreateCaseResponse = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("CreateCaseResponse.case_id required")
    if "caseArn" in data:
        out["case_arn"] = data["caseArn"]
    else:
        raise DeserializationError("CreateCaseResponse.case_arn required")
    return out
