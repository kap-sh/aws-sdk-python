"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanGateAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanGateAttribute: TypeAlias = Literal[
    "Emergency",
    "KeyAccess",
    "PermissionRequired",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanGateAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanGateAttribute:
    return cast(RouteSpanGateAttribute, data)
