"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_hazardous_cargo_type

IsolineHazardousCargoTypeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.isoline_hazardous_cargo_type.IsolineHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineHazardousCargoTypeList) -> list:
    import aws_sdk_geo_routes.types.isoline_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.isoline_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IsolineHazardousCargoTypeList:
    import aws_sdk_geo_routes.types.isoline_hazardous_cargo_type

    out: IsolineHazardousCargoTypeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.isoline_hazardous_cargo_type.deserialize_json(item)
        )
    return out
