"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceAreaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_avoidance_area

IsolineAvoidanceAreaList: TypeAlias = list[
    "aws_sdk_geo_routes.types.isoline_avoidance_area.IsolineAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceAreaList) -> list:
    import aws_sdk_geo_routes.types.isoline_avoidance_area

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.isoline_avoidance_area.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineAvoidanceAreaList:
    import aws_sdk_geo_routes.types.isoline_avoidance_area

    out: IsolineAvoidanceAreaList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.isoline_avoidance_area.deserialize_json(item)
        )
    return out
