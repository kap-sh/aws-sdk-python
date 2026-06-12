"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAttributionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteAttributionType: TypeAlias = Literal[
    "Disclaimer",
    "Tariff",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disclaimer",
        "Tariff",
    )
)


def serialize_json(value: RouteAttributionType) -> str:
    return value


def deserialize_json(data: str) -> RouteAttributionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteAttributionType value: {data!r}")
    return cast(RouteAttributionType, data)
