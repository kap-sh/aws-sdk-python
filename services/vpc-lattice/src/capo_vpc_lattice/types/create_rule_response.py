"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.rule_arn
    import capo_vpc_lattice.types.rule_id
    import capo_vpc_lattice.types.rule_match
    import capo_vpc_lattice.types.rule_name
    import capo_vpc_lattice.types.rule_priority


class CreateRuleResponse(TypedDict, closed=True):
    arn: NotRequired["capo_vpc_lattice.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    id: NotRequired["capo_vpc_lattice.types.rule_id.RuleId"]
    """<p>The ID of the rule.</p>"""
    name: NotRequired["capo_vpc_lattice.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    match: NotRequired["capo_vpc_lattice.types.rule_match.RuleMatch"]
    """<p>The rule match. The <code>RuleMatch</code> must be an <code>HttpMatch</code>. This means that the rule should be an exact match on HTTP constraints which are made up of the HTTP method, path, and header.</p>"""
    priority: NotRequired["capo_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The priority assigned to the rule. The lower the priority number the higher the priority.</p>"""
    action: NotRequired["capo_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The rule action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "match" in value:
        import capo_vpc_lattice.types.rule_match

        out["match"] = capo_vpc_lattice.types.rule_match.serialize_json(value["match"])
    if "priority" in value:
        out["priority"] = value["priority"]
    if "action" in value:
        import capo_vpc_lattice.types.rule_action

        out["action"] = capo_vpc_lattice.types.rule_action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> CreateRuleResponse:
    out: CreateRuleResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "match" in data:
        import capo_vpc_lattice.types.rule_match

        out["match"] = capo_vpc_lattice.types.rule_match.deserialize_json(data["match"])
    if "priority" in data:
        out["priority"] = data["priority"]
    if "action" in data:
        import capo_vpc_lattice.types.rule_action

        out["action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["action"]
        )
    return out
