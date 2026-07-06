"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTruckOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.dimension_centimeters
    import aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list
    import aws_sdk_geo_routes.types.road_snap_trailer_options
    import aws_sdk_geo_routes.types.tunnel_restriction_code
    import aws_sdk_geo_routes.types.weight_kilograms


class RoadSnapTruckOptions(TypedDict, closed=True):
    gross_weight: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Gross weight of the vehicle including trailers, and goods at capacity.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    hazardous_cargos: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list.RoadSnapHazardousCargoTypeList"
    ]
    """<p>List of Hazardous cargos contained in the vehicle.</p>"""
    height: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Height of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    length: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Length of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    trailer: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_trailer_options.RoadSnapTrailerOptions"
    ]
    """<p>Trailer options corresponding to the vehicle.</p>"""
    tunnel_restriction_code: NotRequired[
        "aws_sdk_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""
    width: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Width of the vehicle in centimeters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTruckOptions) -> dict:
    out: dict = {}
    out["GrossWeight"] = value.get("gross_weight", 0)
    if "hazardous_cargos" in value:
        import aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list

        out["HazardousCargos"] = (
            aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list.serialize_json(
                value["hazardous_cargos"]
            )
        )
    out["Height"] = value.get("height", 0)
    out["Length"] = value.get("length", 0)
    if "trailer" in value:
        import aws_sdk_geo_routes.types.road_snap_trailer_options

        out["Trailer"] = (
            aws_sdk_geo_routes.types.road_snap_trailer_options.serialize_json(
                value["trailer"]
            )
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    out["Width"] = value.get("width", 0)
    return out


def deserialize_json(data: dict) -> RoadSnapTruckOptions:
    out: RoadSnapTruckOptions = {}  # type: ignore[typeddict-item]
    if "GrossWeight" in data:
        out["gross_weight"] = data["GrossWeight"]
    else:
        out["gross_weight"] = 0
    if "HazardousCargos" in data:
        import aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            aws_sdk_geo_routes.types.road_snap_hazardous_cargo_type_list.deserialize_json(
                data["HazardousCargos"]
            )
        )
    if "Height" in data:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    if "Length" in data:
        out["length"] = data["Length"]
    else:
        out["length"] = 0
    if "Trailer" in data:
        import aws_sdk_geo_routes.types.road_snap_trailer_options

        out["trailer"] = (
            aws_sdk_geo_routes.types.road_snap_trailer_options.deserialize_json(
                data["Trailer"]
            )
        )
    if "TunnelRestrictionCode" in data:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    if "Width" in data:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    return out
