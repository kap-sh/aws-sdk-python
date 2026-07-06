"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListRoutingRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule
    import aws_sdk_apigatewayv2.types.next_token


class ListRoutingRulesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_apigatewayv2.types.next_token.NextToken"]
    routing_rules: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule.__listOfRoutingRule"
    ]
    """<p>The routing rules.<p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "routing_rules" in value:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule

        out["routingRules"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule.serialize_json(
                value["routing_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRoutingRulesResponse:
    out: ListRoutingRulesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "routingRules" in data:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule

        out["routing_rules"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule.deserialize_json(
                data["routingRules"]
            )
        )
    return out
