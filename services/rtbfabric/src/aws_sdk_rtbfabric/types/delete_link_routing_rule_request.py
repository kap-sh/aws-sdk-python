"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.rule_id


class DeleteLinkRoutingRuleRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLinkRoutingRuleRequest:
    out: DeleteLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    return out
