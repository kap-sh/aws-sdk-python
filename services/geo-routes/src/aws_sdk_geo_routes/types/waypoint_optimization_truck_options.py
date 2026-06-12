"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTruckOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.dimension_centimeters
    import aws_sdk_geo_routes.types.tunnel_restriction_code
    import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list
    import aws_sdk_geo_routes.types.waypoint_optimization_trailer_options
    import aws_sdk_geo_routes.types.waypoint_optimization_truck_type
    import aws_sdk_geo_routes.types.weight_kilograms


class WaypointOptimizationTruckOptions(TypedDict):
    gross_weight: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Gross weight of the vehicle including trailers, and goods at capacity.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    hazardous_cargos: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.WaypointOptimizationHazardousCargoTypeList"
    ]
    """<p>List of Hazardous cargo contained in the vehicle.</p>"""
    height: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Height of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    length: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Length of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    trailer: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_trailer_options.WaypointOptimizationTrailerOptions"
    ]
    """<p>Trailer options corresponding to the vehicle.</p>"""
    truck_type: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_truck_type.WaypointOptimizationTruckType"
    ]
    """<p>The type of truck: <code>LightTruck</code> for smaller delivery vehicles, <code> StraightTruck</code> for rigid body trucks, or <code>Tractor</code> for tractor-trailer combinations.</p>"""
    tunnel_restriction_code: NotRequired[
        "aws_sdk_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""
    weight_per_axle: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    width: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Width of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTruckOptions) -> dict:
    out: dict = {}
    out["GrossWeight"] = value.get("gross_weight", 0)
    if "hazardous_cargos" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list

        out["HazardousCargos"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.serialize_json(
                value["hazardous_cargos"]
            )
        )
    out["Height"] = value.get("height", 0)
    out["Length"] = value.get("length", 0)
    if "trailer" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_trailer_options

        out["Trailer"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_trailer_options.serialize_json(
                value["trailer"]
            )
        )
    if "truck_type" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_truck_type

        out["TruckType"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_truck_type.serialize_json(
                value["truck_type"]
            )
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    out["WeightPerAxle"] = value.get("weight_per_axle", 0)
    out["Width"] = value.get("width", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTruckOptions:
    out: WaypointOptimizationTruckOptions = {}  # type: ignore[typeddict-item]
    if "GrossWeight" in data:
        out["gross_weight"] = data["GrossWeight"]
    else:
        out["gross_weight"] = 0
    if "HazardousCargos" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type_list.deserialize_json(
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
        import aws_sdk_geo_routes.types.waypoint_optimization_trailer_options

        out["trailer"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_trailer_options.deserialize_json(
                data["Trailer"]
            )
        )
    if "TruckType" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_truck_type

        out["truck_type"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_truck_type.deserialize_json(
                data["TruckType"]
            )
        )
    if "TunnelRestrictionCode" in data:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    if "WeightPerAxle" in data:
        out["weight_per_axle"] = data["WeightPerAxle"]
    else:
        out["weight_per_axle"] = 0
    if "Width" in data:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    return out
