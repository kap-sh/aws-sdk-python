"""Generated from Smithy shape ``com.amazonaws.georoutes#GeometryFormat``."""

from typing import Literal, TypeAlias, cast

GeometryFormat: TypeAlias = Literal[
    "FlexiblePolyline",
    "Simple",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeometryFormat) -> str:
    return value


def deserialize_json(data: str) -> GeometryFormat:
    return cast(GeometryFormat, data)
