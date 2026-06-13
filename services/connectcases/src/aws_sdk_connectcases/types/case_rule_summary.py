"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_arn
    import aws_sdk_connectcases.types.case_rule_description
    import aws_sdk_connectcases.types.case_rule_id
    import aws_sdk_connectcases.types.case_rule_name
    import aws_sdk_connectcases.types.rule_type


class CaseRuleSummary(TypedDict):
    case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    name: "aws_sdk_connectcases.types.case_rule_name.CaseRuleName"
    """<p>Name of the case rule.</p>"""
    case_rule_arn: "aws_sdk_connectcases.types.case_rule_arn.CaseRuleArn"
    """<p>The Amazon Resource Name (ARN) of the case rule. </p>"""
    rule_type: "aws_sdk_connectcases.types.rule_type.RuleType"
    """<p>Possible types for a rule.</p>"""
    description: NotRequired[
        "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>Description of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleSummary) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["name"] = value["name"]
    out["caseRuleArn"] = value["case_rule_arn"]
    out["ruleType"] = value["rule_type"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CaseRuleSummary:
    out: CaseRuleSummary = {}  # type: ignore[typeddict-item]
    if "caseRuleId" in data:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        raise DeserializationError("CaseRuleSummary.case_rule_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CaseRuleSummary.name required")
    if "caseRuleArn" in data:
        out["case_rule_arn"] = data["caseRuleArn"]
    else:
        raise DeserializationError("CaseRuleSummary.case_rule_arn required")
    if "ruleType" in data:
        out["rule_type"] = data["ruleType"]
    else:
        raise DeserializationError("CaseRuleSummary.rule_type required")
    if "description" in data:
        out["description"] = data["description"]
    return out
