"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.rule_id


class GetLinkRoutingRuleRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "capo_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLinkRoutingRuleRequest:
    out: GetLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    return out
