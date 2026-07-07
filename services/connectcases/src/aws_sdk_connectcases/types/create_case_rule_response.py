"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_arn
    import aws_sdk_connectcases.types.case_rule_id


class CreateCaseRuleResponse(TypedDict, closed=True):
    case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    case_rule_arn: "aws_sdk_connectcases.types.case_rule_arn.CaseRuleArn"
    """<p>The Amazon Resource Name (ARN) of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRuleResponse) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["caseRuleArn"] = value["case_rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateCaseRuleResponse:
    out: CreateCaseRuleResponse = {}  # type: ignore[typeddict-item]
    if "caseRuleId" in data:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        raise DeserializationError("CreateCaseRuleResponse.case_rule_id required")
    if "caseRuleArn" in data:
        out["case_rule_arn"] = data["caseRuleArn"]
    else:
        raise DeserializationError("CreateCaseRuleResponse.case_rule_arn required")
    return out
