"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanGateAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanGateAttribute: TypeAlias = Literal[
    "Emergency",
    "KeyAccess",
    "PermissionRequired",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Emergency",
        "KeyAccess",
        "PermissionRequired",
    )
)


def serialize_json(value: RouteSpanGateAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanGateAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteSpanGateAttribute value: {data!r}")
    return cast(RouteSpanGateAttribute, data)
