"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetRoutingRuleRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    routing_rule_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The routing rule ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoutingRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRoutingRuleRequest:
    out: GetRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    return out
