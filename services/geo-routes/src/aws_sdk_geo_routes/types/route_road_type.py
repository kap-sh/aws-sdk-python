"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoadType``."""

from typing import Literal, TypeAlias, cast

RouteRoadType: TypeAlias = Literal[
    "Highway",
    "Rural",
    "Urban",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRoadType) -> str:
    return value


def deserialize_json(data: str) -> RouteRoadType:
    return cast(RouteRoadType, data)
