"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNoticeImpact``."""

from typing import Literal, TypeAlias, cast

RouteNoticeImpact: TypeAlias = Literal[
    "High",
    "Low",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteNoticeImpact) -> str:
    return value


def deserialize_json(data: str) -> RouteNoticeImpact:
    return cast(RouteNoticeImpact, data)
