"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAttribute``."""

from typing import Literal, TypeAlias, cast

RouteAccessibilityAttribute: TypeAlias = Literal["Wheelchair",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessibilityAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteAccessibilityAttribute:
    return cast(RouteAccessibilityAttribute, data)
