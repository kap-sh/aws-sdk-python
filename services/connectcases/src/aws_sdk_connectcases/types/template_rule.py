"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_id
    import aws_sdk_connectcases.types.field_id


class TemplateRule(TypedDict, closed=True):
    case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateRule) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["fieldId"] = value.get("field_id", "NULL")
    return out


def deserialize_json(data: dict) -> TemplateRule:
    out: TemplateRule = {}  # type: ignore[typeddict-item]
    if "caseRuleId" in data:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        raise DeserializationError("TemplateRule.case_rule_id required")
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = "NULL"
    return out
