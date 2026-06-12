"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRoadType: TypeAlias = Literal[
    "Highway",
    "Rural",
    "Urban",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Highway",
        "Rural",
        "Urban",
    )
)


def serialize_json(value: RouteRoadType) -> str:
    return value


def deserialize_json(data: str) -> RouteRoadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteRoadType value: {data!r}")
    return cast(RouteRoadType, data)
