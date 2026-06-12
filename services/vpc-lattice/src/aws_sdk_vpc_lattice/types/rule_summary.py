"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.rule_arn
    import aws_sdk_vpc_lattice.types.rule_id
    import aws_sdk_vpc_lattice.types.rule_name
    import aws_sdk_vpc_lattice.types.rule_priority
    import aws_sdk_vpc_lattice.types.timestamp


class RuleSummary(TypedDict):
    arn: NotRequired["aws_sdk_vpc_lattice.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    id: NotRequired["aws_sdk_vpc_lattice.types.rule_id.RuleId"]
    """<p>The ID of the rule.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    is_default: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether this is the default listener rule.</p>"""
    priority: NotRequired["aws_sdk_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The priority of the rule.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener rule was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener rule was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "is_default" in value:
        out["isDefault"] = value["is_default"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "isDefault" in data:
        out["is_default"] = data["isDefault"]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
