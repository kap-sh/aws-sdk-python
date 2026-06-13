"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.rule_id


class GetLinkRoutingRuleRequest(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLinkRoutingRuleRequest:
    out: GetLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    return out
