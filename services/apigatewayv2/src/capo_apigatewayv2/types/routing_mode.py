"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingMode``."""

from typing import Literal, TypeAlias, cast

RoutingMode: TypeAlias = Literal[
    "API_MAPPING_ONLY",
    "ROUTING_RULE_ONLY",
    "ROUTING_RULE_THEN_API_MAPPING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingMode) -> str:
    return value


def deserialize_json(data: str) -> RoutingMode:
    return cast(RoutingMode, data)
