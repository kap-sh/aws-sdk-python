"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_details
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.domain_id


class CreateCaseRuleRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    name: "capo_connectcases.types.case_rule_name.CaseRuleName"
    """<p>Name of the case rule.</p>"""
    description: NotRequired[
        "capo_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>The description of a case rule.</p>"""
    rule: "capo_connectcases.types.case_rule_details.CaseRuleDetails"
    """<p>Represents what rule type should take place, under what conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_connectcases.types.case_rule_details

    out["rule"] = capo_connectcases.types.case_rule_details.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> CreateCaseRuleRequest:
    out: CreateCaseRuleRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCaseRuleRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "rule" in data:
        import capo_connectcases.types.case_rule_details

        out["rule"] = capo_connectcases.types.case_rule_details.deserialize_json(
            data["rule"]
        )
    else:
        raise DeserializationError("CreateCaseRuleRequest.rule required")
    return out
