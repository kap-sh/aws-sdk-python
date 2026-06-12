"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteEngineType: TypeAlias = Literal[
    "Electric",
    "InternalCombustion",
    "PluginHybrid",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Electric",
        "InternalCombustion",
        "PluginHybrid",
    )
)


def serialize_json(value: RouteEngineType) -> str:
    return value


def deserialize_json(data: str) -> RouteEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteEngineType value: {data!r}")
    return cast(RouteEngineType, data)
