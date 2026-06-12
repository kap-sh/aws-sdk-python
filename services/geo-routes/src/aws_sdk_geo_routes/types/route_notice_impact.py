"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNoticeImpact``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteNoticeImpact: TypeAlias = Literal[
    "High",
    "Low",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "High",
        "Low",
    )
)


def serialize_json(value: RouteNoticeImpact) -> str:
    return value


def deserialize_json(data: str) -> RouteNoticeImpact:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteNoticeImpact value: {data!r}")
    return cast(RouteNoticeImpact, data)
