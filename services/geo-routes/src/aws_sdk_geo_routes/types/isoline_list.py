"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline

IsolineList: TypeAlias = list["aws_sdk_geo_routes.types.isoline.Isoline"]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineList) -> list:
    import aws_sdk_geo_routes.types.isoline

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.isoline.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineList:
    import aws_sdk_geo_routes.types.isoline

    out: IsolineList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.isoline.deserialize_json(item))
    return out
