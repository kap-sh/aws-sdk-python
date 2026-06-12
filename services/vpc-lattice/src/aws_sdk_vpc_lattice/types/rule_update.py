"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.rule_identifier
    import aws_sdk_vpc_lattice.types.rule_match
    import aws_sdk_vpc_lattice.types.rule_priority


class RuleUpdate(TypedDict):
    rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier"
    """<p>The ID or ARN of the rule.</p>"""
    match: NotRequired["aws_sdk_vpc_lattice.types.rule_match.RuleMatch"]
    """<p>The rule match.</p>"""
    priority: NotRequired["aws_sdk_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The rule priority. A listener can't have multiple rules with the same priority.</p>"""
    action: NotRequired["aws_sdk_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The rule action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdate) -> dict:
    out: dict = {}
    out["ruleIdentifier"] = value["rule_identifier"]
    if "match" in value:
        import aws_sdk_vpc_lattice.types.rule_match

        out["match"] = aws_sdk_vpc_lattice.types.rule_match.serialize_json(
            value["match"]
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "action" in value:
        import aws_sdk_vpc_lattice.types.rule_action

        out["action"] = aws_sdk_vpc_lattice.types.rule_action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> RuleUpdate:
    out: RuleUpdate = {}  # type: ignore[typeddict-item]
    if "ruleIdentifier" in data:
        out["rule_identifier"] = data["ruleIdentifier"]
    else:
        raise DeserializationError("RuleUpdate.rule_identifier required")
    if "match" in data:
        import aws_sdk_vpc_lattice.types.rule_match

        out["match"] = aws_sdk_vpc_lattice.types.rule_match.deserialize_json(
            data["match"]
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "action" in data:
        import aws_sdk_vpc_lattice.types.rule_action

        out["action"] = aws_sdk_vpc_lattice.types.rule_action.deserialize_json(
            data["action"]
        )
    return out
