"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.rule_match
    import aws_sdk_vpc_lattice.types.rule_name
    import aws_sdk_vpc_lattice.types.rule_priority
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.tag_map


class CreateRuleRequest(TypedDict):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""
    name: "aws_sdk_vpc_lattice.types.rule_name.RuleName"
    """<p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    match: "aws_sdk_vpc_lattice.types.rule_match.RuleMatch"
    """<p>The rule match.</p>"""
    priority: "aws_sdk_vpc_lattice.types.rule_priority.RulePriority"
    """<p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>"""
    action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction"
    """<p>The action for the default rule.</p>"""
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_vpc_lattice.types.rule_match

    out["match"] = aws_sdk_vpc_lattice.types.rule_match.serialize_json(value["match"])
    out["priority"] = value["priority"]
    import aws_sdk_vpc_lattice.types.rule_action

    out["action"] = aws_sdk_vpc_lattice.types.rule_action.serialize_json(
        value["action"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRuleRequest:
    out: CreateRuleRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleRequest.name required")
    if "match" in data:
        import aws_sdk_vpc_lattice.types.rule_match

        out["match"] = aws_sdk_vpc_lattice.types.rule_match.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.match required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateRuleRequest.priority required")
    if "action" in data:
        import aws_sdk_vpc_lattice.types.rule_action

        out["action"] = aws_sdk_vpc_lattice.types.rule_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.action required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
