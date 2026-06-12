"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.rule_identifier
    import aws_sdk_vpc_lattice.types.rule_match
    import aws_sdk_vpc_lattice.types.rule_priority
    import aws_sdk_vpc_lattice.types.service_identifier


class UpdateRuleRequest(TypedDict):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""
    rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier"
    """<p>The ID or ARN of the rule.</p>"""
    match: NotRequired["aws_sdk_vpc_lattice.types.rule_match.RuleMatch"]
    """<p>The rule match.</p>"""
    priority: NotRequired["aws_sdk_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The rule priority. A listener can't have multiple rules with the same priority.</p>"""
    action: NotRequired["aws_sdk_vpc_lattice.types.rule_action.RuleAction"]
    """<p>Information about the action for the specified listener rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateRuleRequest:
    out: UpdateRuleRequest = {}  # type: ignore[typeddict-item]
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
