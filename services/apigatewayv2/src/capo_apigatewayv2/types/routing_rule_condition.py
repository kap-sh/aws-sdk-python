"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.routing_rule_match_base_paths
    import capo_apigatewayv2.types.routing_rule_match_headers


class RoutingRuleCondition(TypedDict, closed=True):
    match_base_paths: NotRequired[
        "capo_apigatewayv2.types.routing_rule_match_base_paths.RoutingRuleMatchBasePaths"
    ]
    """<p>The base path to be matched.</p>"""
    match_headers: NotRequired[
        "capo_apigatewayv2.types.routing_rule_match_headers.RoutingRuleMatchHeaders"
    ]
    """<p>The headers to be matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleCondition) -> dict:
    out: dict = {}
    if "match_base_paths" in value:
        import capo_apigatewayv2.types.routing_rule_match_base_paths

        out["matchBasePaths"] = (
            capo_apigatewayv2.types.routing_rule_match_base_paths.serialize_json(
                value["match_base_paths"]
            )
        )
    if "match_headers" in value:
        import capo_apigatewayv2.types.routing_rule_match_headers

        out["matchHeaders"] = (
            capo_apigatewayv2.types.routing_rule_match_headers.serialize_json(
                value["match_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingRuleCondition:
    out: RoutingRuleCondition = {}  # type: ignore[typeddict-item]
    if "matchBasePaths" in data:
        import capo_apigatewayv2.types.routing_rule_match_base_paths

        out["match_base_paths"] = (
            capo_apigatewayv2.types.routing_rule_match_base_paths.deserialize_json(
                data["matchBasePaths"]
            )
        )
    if "matchHeaders" in data:
        import capo_apigatewayv2.types.routing_rule_match_headers

        out["match_headers"] = (
            capo_apigatewayv2.types.routing_rule_match_headers.deserialize_json(
                data["matchHeaders"]
            )
        )
    return out
