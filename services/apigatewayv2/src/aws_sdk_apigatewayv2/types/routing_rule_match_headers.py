"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleMatchHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value


class RoutingRuleMatchHeaders(TypedDict, closed=True):
    any_of: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value.__listOfRoutingRuleMatchHeaderValue"
    ]
    """<p>The header name and header value glob to be matched. The matchHeaders condition is matched if any of the header name and header value globs are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleMatchHeaders) -> dict:
    out: dict = {}
    if "any_of" in value:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value

        out["anyOf"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value.serialize_json(
                value["any_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingRuleMatchHeaders:
    out: RoutingRuleMatchHeaders = {}  # type: ignore[typeddict-item]
    if "anyOf" in data:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value

        out["any_of"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_match_header_value.deserialize_json(
                data["anyOf"]
            )
        )
    return out
