"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteAccessibilityAttribute: TypeAlias = Literal["Wheelchair",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Wheelchair",))


def serialize_json(value: RouteAccessibilityAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteAccessibilityAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteAccessibilityAttribute value: {data!r}"
        )
    return cast(RouteAccessibilityAttribute, data)
