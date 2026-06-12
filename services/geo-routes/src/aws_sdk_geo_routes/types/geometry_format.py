"""Generated from Smithy shape ``com.amazonaws.georoutes#GeometryFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

GeometryFormat: TypeAlias = Literal[
    "FlexiblePolyline",
    "Simple",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FlexiblePolyline",
        "Simple",
    )
)


def serialize_json(value: GeometryFormat) -> str:
    return value


def deserialize_json(data: str) -> GeometryFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeometryFormat value: {data!r}")
    return cast(GeometryFormat, data)
