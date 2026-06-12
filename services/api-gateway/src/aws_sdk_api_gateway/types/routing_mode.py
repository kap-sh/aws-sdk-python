"""Generated from Smithy shape ``com.amazonaws.apigateway#RoutingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

RoutingMode: TypeAlias = Literal[
    "BASE_PATH_MAPPING_ONLY",
    "ROUTING_RULE_ONLY",
    "ROUTING_RULE_THEN_BASE_PATH_MAPPING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASE_PATH_MAPPING_ONLY",
        "ROUTING_RULE_ONLY",
        "ROUTING_RULE_THEN_BASE_PATH_MAPPING",
    )
)


def serialize_json(value: RoutingMode) -> str:
    return value


def deserialize_json(data: str) -> RoutingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingMode value: {data!r}")
    return cast(RoutingMode, data)
