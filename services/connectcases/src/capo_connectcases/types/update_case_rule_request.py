"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateCaseRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_details
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.domain_id


class UpdateCaseRuleRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    name: NotRequired["capo_connectcases.types.case_rule_name.CaseRuleName"]
    """<p>Name of the case rule.</p>"""
    description: NotRequired[
        "capo_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>Description of a case rule.</p>"""
    rule: NotRequired["capo_connectcases.types.case_rule_details.CaseRuleDetails"]
    """<p>Represents what rule type should take place, under what conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseRuleRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule" in value:
        import capo_connectcases.types.case_rule_details

        out["rule"] = capo_connectcases.types.case_rule_details.serialize_json(
            value["rule"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCaseRuleRequest:
    out: UpdateCaseRuleRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "rule" in data:
        import capo_connectcases.types.case_rule_details

        out["rule"] = capo_connectcases.types.case_rule_details.deserialize_json(
            data["rule"]
        )
    return out
