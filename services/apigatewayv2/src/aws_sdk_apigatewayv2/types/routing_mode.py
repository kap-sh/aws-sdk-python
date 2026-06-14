"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

RoutingMode: TypeAlias = Literal[
    "API_MAPPING_ONLY",
    "ROUTING_RULE_ONLY",
    "ROUTING_RULE_THEN_API_MAPPING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API_MAPPING_ONLY",
        "ROUTING_RULE_ONLY",
        "ROUTING_RULE_THEN_API_MAPPING",
    )
)


def serialize_json(value: RoutingMode) -> str:
    return value


def deserialize_json(data: str) -> RoutingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingMode value: {data!r}")
    return cast(RoutingMode, data)
