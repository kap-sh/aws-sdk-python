"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdateSuccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.rule_arn
    import aws_sdk_vpc_lattice.types.rule_id
    import aws_sdk_vpc_lattice.types.rule_match
    import aws_sdk_vpc_lattice.types.rule_name
    import aws_sdk_vpc_lattice.types.rule_priority


class RuleUpdateSuccess(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_vpc_lattice.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    id: NotRequired["aws_sdk_vpc_lattice.types.rule_id.RuleId"]
    """<p>The ID of the listener.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.rule_name.RuleName"]
    """<p>The name of the listener.</p>"""
    is_default: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether this is the default rule.</p>"""
    match: NotRequired["aws_sdk_vpc_lattice.types.rule_match.RuleMatch"]
    """<p>The rule match.</p>"""
    priority: NotRequired["aws_sdk_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The rule priority.</p>"""
    action: NotRequired["aws_sdk_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The action for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdateSuccess) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "is_default" in value:
        out["isDefault"] = value["is_default"]
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


def deserialize_json(data: dict) -> RuleUpdateSuccess:
    out: RuleUpdateSuccess = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "isDefault" in data:
        out["is_default"] = data["isDefault"]
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
