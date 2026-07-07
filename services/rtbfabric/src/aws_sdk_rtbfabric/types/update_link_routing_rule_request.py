"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.rule_condition
    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_priority


class UpdateLinkRoutingRuleRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    priority: "aws_sdk_rtbfabric.types.rule_priority.RulePriority"
    """<p>The updated priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.</p>"""
    conditions: "aws_sdk_rtbfabric.types.rule_condition.RuleCondition"
    """<p>The updated conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    out["priority"] = value["priority"]
    import aws_sdk_rtbfabric.types.rule_condition

    out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkRoutingRuleRequest:
    out: UpdateLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("UpdateLinkRoutingRuleRequest.priority required")
    if "conditions" in data:
        import aws_sdk_rtbfabric.types.rule_condition

        out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("UpdateLinkRoutingRuleRequest.conditions required")
    return out
