"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_connection

IsolineConnectionList: TypeAlias = list[
    "aws_sdk_geo_routes.types.isoline_connection.IsolineConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineConnectionList) -> list:
    import aws_sdk_geo_routes.types.isoline_connection

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.isoline_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineConnectionList:
    import aws_sdk_geo_routes.types.isoline_connection

    out: IsolineConnectionList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.isoline_connection.deserialize_json(item))
    return out
