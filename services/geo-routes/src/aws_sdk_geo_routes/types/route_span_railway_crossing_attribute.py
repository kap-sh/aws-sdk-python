"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanRailwayCrossingAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanRailwayCrossingAttribute: TypeAlias = Literal[
    "Protected",
    "Unprotected",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Protected",
        "Unprotected",
    )
)


def serialize_json(value: RouteSpanRailwayCrossingAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanRailwayCrossingAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanRailwayCrossingAttribute value: {data!r}"
        )
    return cast(RouteSpanRailwayCrossingAttribute, data)
