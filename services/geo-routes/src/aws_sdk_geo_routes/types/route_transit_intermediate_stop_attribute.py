"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitIntermediateStopAttribute: TypeAlias = Literal[
    "NoEntry",
    "NoExit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoEntry",
        "NoExit",
    )
)


def serialize_json(value: RouteTransitIntermediateStopAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIntermediateStopAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTransitIntermediateStopAttribute value: {data!r}"
        )
    return cast(RouteTransitIntermediateStopAttribute, data)
