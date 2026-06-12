"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_id


class CaseRuleError(TypedDict):
    id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>The case rule identifier that caused the error.</p>"""
    error_code: "str"
    """<p>Error code from getting a case rule.</p>"""
    message: NotRequired["str"]
    """<p>Error message from getting a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CaseRuleError:
    out: CaseRuleError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CaseRuleError.id required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("CaseRuleError.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
