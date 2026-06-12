"""Generated from Smithy shape ``com.amazonaws.georoutes#LinearRing``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position

LinearRing: TypeAlias = list["aws_sdk_geo_routes.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRing) -> list:
    import aws_sdk_geo_routes.types.position

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRing:
    import aws_sdk_geo_routes.types.position

    out: LinearRing = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.position.deserialize_json(item))
    return out
