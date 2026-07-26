"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanRailwayCrossingAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanRailwayCrossingAttribute: TypeAlias = Literal[
    "Protected",
    "Unprotected",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanRailwayCrossingAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanRailwayCrossingAttribute:
    return cast(RouteSpanRailwayCrossingAttribute, data)
