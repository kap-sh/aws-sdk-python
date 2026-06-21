"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteEngineType``."""

from typing import Literal, TypeAlias, cast

RouteEngineType: TypeAlias = Literal[
    "Electric",
    "InternalCombustion",
    "PluginHybrid",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteEngineType) -> str:
    return value


def deserialize_json(data: str) -> RouteEngineType:
    return cast(RouteEngineType, data)
