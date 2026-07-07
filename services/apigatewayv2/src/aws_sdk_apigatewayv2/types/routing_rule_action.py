"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api


class RoutingRuleAction(TypedDict, closed=True):
    invoke_api: NotRequired[
        "aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api.RoutingRuleActionInvokeApi"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleAction) -> dict:
    out: dict = {}
    if "invoke_api" in value:
        import aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api

        out["invokeApi"] = (
            aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api.serialize_json(
                value["invoke_api"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingRuleAction:
    out: RoutingRuleAction = {}  # type: ignore[typeddict-item]
    if "invokeApi" in data:
        import aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api

        out["invoke_api"] = (
            aws_sdk_apigatewayv2.types.routing_rule_action_invoke_api.deserialize_json(
                data["invokeApi"]
            )
        )
    return out
