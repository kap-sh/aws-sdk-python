"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RouteToTargetAction``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.static_route
    import aws_sdk_bedrock_agentcore_control.types.weighted_route


class _RouteToTargetAction_staticRoute(TypedDict):
    staticRoute: "aws_sdk_bedrock_agentcore_control.types.static_route.StaticRoute"


class _RouteToTargetAction_weightedRoute(TypedDict):
    weightedRoute: (
        "aws_sdk_bedrock_agentcore_control.types.weighted_route.WeightedRoute"
    )


RouteToTargetAction: TypeAlias = (
    _RouteToTargetAction_staticRoute | _RouteToTargetAction_weightedRoute
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteToTargetAction) -> dict:
    if "staticRoute" in value:
        import aws_sdk_bedrock_agentcore_control.types.static_route

        return {
            "staticRoute": aws_sdk_bedrock_agentcore_control.types.static_route.serialize_json(
                value["staticRoute"]
            )
        }
    elif "weightedRoute" in value:
        import aws_sdk_bedrock_agentcore_control.types.weighted_route

        return {
            "weightedRoute": aws_sdk_bedrock_agentcore_control.types.weighted_route.serialize_json(
                value["weightedRoute"]
            )
        }
    else:
        raise SerializationError("RouteToTargetAction: no variant present")


def deserialize_json(data: dict) -> RouteToTargetAction:
    if "staticRoute" in data:
        import aws_sdk_bedrock_agentcore_control.types.static_route

        return {
            "staticRoute": aws_sdk_bedrock_agentcore_control.types.static_route.deserialize_json(
                data["staticRoute"]
            )
        }
    elif "weightedRoute" in data:
        import aws_sdk_bedrock_agentcore_control.types.weighted_route

        return {
            "weightedRoute": aws_sdk_bedrock_agentcore_control.types.weighted_route.deserialize_json(
                data["weightedRoute"]
            )
        }
    else:
        raise DeserializationError("RouteToTargetAction: no recognized variant key")
