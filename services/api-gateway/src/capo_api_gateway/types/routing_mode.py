"""Generated from Smithy shape ``com.amazonaws.apigateway#RoutingMode``."""

from typing import Literal, TypeAlias, cast

RoutingMode: TypeAlias = Literal[
    "BASE_PATH_MAPPING_ONLY",
    "ROUTING_RULE_ONLY",
    "ROUTING_RULE_THEN_BASE_PATH_MAPPING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingMode) -> str:
    return value


def deserialize_json(data: str) -> RoutingMode:
    return cast(RoutingMode, data)
