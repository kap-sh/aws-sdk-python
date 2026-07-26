"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAttributionType``."""

from typing import Literal, TypeAlias, cast

RouteAttributionType: TypeAlias = Literal[
    "Disclaimer",
    "Tariff",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAttributionType) -> str:
    return value


def deserialize_json(data: str) -> RouteAttributionType:
    return cast(RouteAttributionType, data)
