"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTruckOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.dimension_centimeters
    import aws_sdk_geo_routes.types.route_engine_type
    import aws_sdk_geo_routes.types.route_hazardous_cargo_type_list
    import aws_sdk_geo_routes.types.route_trailer_options
    import aws_sdk_geo_routes.types.route_truck_type
    import aws_sdk_geo_routes.types.route_vehicle_license_plate
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour
    import aws_sdk_geo_routes.types.tunnel_restriction_code
    import aws_sdk_geo_routes.types.weight_kilograms
    import aws_sdk_geo_routes.types.weight_per_axle_group


class RouteTruckOptions(TypedDict, closed=True):
    axle_count: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Total number of axles of the vehicle.</p>"""
    engine_type: NotRequired[
        "aws_sdk_geo_routes.types.route_engine_type.RouteEngineType"
    ]
    """<p>Engine type of the vehicle.</p>"""
    gross_weight: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Gross weight of the vehicle including trailers, and goods at capacity.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    hazardous_cargos: NotRequired[
        "aws_sdk_geo_routes.types.route_hazardous_cargo_type_list.RouteHazardousCargoTypeList"
    ]
    """<p>List of Hazardous cargo contained in the vehicle.</p>"""
    height: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Height of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    height_above_first_axle: (
        "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    )
    """<p>Height of the vehicle above its first axle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    kpra_length: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Kingpin to rear axle length of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""
    length: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Length of the vehicle.</p> <p> <b>Unit</b>: <code>c</code> </p>"""
    license_plate: NotRequired[
        "aws_sdk_geo_routes.types.route_vehicle_license_plate.RouteVehicleLicensePlate"
    ]
    """<p>The vehicle License Plate.</p>"""
    max_speed: NotRequired[
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Maximum speed</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>The number of occupants in the vehicle.</p> <p>Default value: <code>1</code> </p>"""
    payload_capacity: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Payload capacity of the vehicle and trailers attached.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    tire_count: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of tires on the vehicle.</p>"""
    trailer: NotRequired[
        "aws_sdk_geo_routes.types.route_trailer_options.RouteTrailerOptions"
    ]
    """<p>Trailer options corresponding to the vehicle.</p>"""
    truck_type: NotRequired["aws_sdk_geo_routes.types.route_truck_type.RouteTruckType"]
    """<p>The type of truck: <code>LightTruck</code> for smaller delivery vehicles, <code> StraightTruck</code> for rigid body trucks, or <code>Tractor</code> for tractor-trailer combinations.</p>"""
    tunnel_restriction_code: NotRequired[
        "aws_sdk_geo_routes.types.tunnel_restriction_code.TunnelRestrictionCode"
    ]
    """<p>The tunnel restriction code.</p> <p>Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.</p> <ul> <li> <p> <i>Tunnel Category B</i> </p> <ul> <li> <p> <i>Risk Level</i>: Limited risk</p> </li> <li> <p> <i>Restrictions</i>: Few restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category C</i> </p> <ul> <li> <p> <i>Risk Level</i>: Medium risk</p> </li> <li> <p> <i>Restrictions</i>: Some restrictions</p> </li> </ul> </li> <li> <p> <i>Tunnel Category D</i> </p> <ul> <li> <p> <i>Risk Level</i>: High risk</p> </li> <li> <p> <i>Restrictions</i>: Many restrictions occur</p> </li> </ul> </li> <li> <p> <i>Tunnel Category E</i> </p> <ul> <li> <p> <i>Risk Level</i>: Very high risk</p> </li> <li> <p> <i>Restrictions</i>: Restricted tunnel</p> </li> </ul> </li> </ul>"""
    weight_per_axle: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    weight_per_axle_group: NotRequired[
        "aws_sdk_geo_routes.types.weight_per_axle_group.WeightPerAxleGroup"
    ]
    """<p>Specifies the total weight for the specified axle group. Meant for usage in countries that have different regulations based on the axle group type.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    width: "aws_sdk_geo_routes.types.dimension_centimeters.DimensionCentimeters"
    """<p>Width of the vehicle.</p> <p> <b>Unit</b>: <code>centimeters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTruckOptions) -> dict:
    out: dict = {}
    if "axle_count" in value:
        out["AxleCount"] = value["axle_count"]
    if "engine_type" in value:
        import aws_sdk_geo_routes.types.route_engine_type

        out["EngineType"] = aws_sdk_geo_routes.types.route_engine_type.serialize_json(
            value["engine_type"]
        )
    out["GrossWeight"] = value.get("gross_weight", 0)
    if "hazardous_cargos" in value:
        import aws_sdk_geo_routes.types.route_hazardous_cargo_type_list

        out["HazardousCargos"] = (
            aws_sdk_geo_routes.types.route_hazardous_cargo_type_list.serialize_json(
                value["hazardous_cargos"]
            )
        )
    out["Height"] = value.get("height", 0)
    out["HeightAboveFirstAxle"] = value.get("height_above_first_axle", 0)
    out["KpraLength"] = value.get("kpra_length", 0)
    out["Length"] = value.get("length", 0)
    if "license_plate" in value:
        import aws_sdk_geo_routes.types.route_vehicle_license_plate

        out["LicensePlate"] = (
            aws_sdk_geo_routes.types.route_vehicle_license_plate.serialize_json(
                value["license_plate"]
            )
        )
    if "max_speed" in value:
        out["MaxSpeed"] = value["max_speed"]
    if "occupancy" in value:
        out["Occupancy"] = value["occupancy"]
    out["PayloadCapacity"] = value.get("payload_capacity", 0)
    if "tire_count" in value:
        out["TireCount"] = value["tire_count"]
    if "trailer" in value:
        import aws_sdk_geo_routes.types.route_trailer_options

        out["Trailer"] = aws_sdk_geo_routes.types.route_trailer_options.serialize_json(
            value["trailer"]
        )
    if "truck_type" in value:
        import aws_sdk_geo_routes.types.route_truck_type

        out["TruckType"] = aws_sdk_geo_routes.types.route_truck_type.serialize_json(
            value["truck_type"]
        )
    if "tunnel_restriction_code" in value:
        out["TunnelRestrictionCode"] = value["tunnel_restriction_code"]
    out["WeightPerAxle"] = value.get("weight_per_axle", 0)
    if "weight_per_axle_group" in value:
        import aws_sdk_geo_routes.types.weight_per_axle_group

        out["WeightPerAxleGroup"] = (
            aws_sdk_geo_routes.types.weight_per_axle_group.serialize_json(
                value["weight_per_axle_group"]
            )
        )
    out["Width"] = value.get("width", 0)
    return out


def deserialize_json(data: dict) -> RouteTruckOptions:
    out: RouteTruckOptions = {}  # type: ignore[typeddict-item]
    if "AxleCount" in data:
        out["axle_count"] = data["AxleCount"]
    if "EngineType" in data:
        import aws_sdk_geo_routes.types.route_engine_type

        out["engine_type"] = (
            aws_sdk_geo_routes.types.route_engine_type.deserialize_json(
                data["EngineType"]
            )
        )
    if "GrossWeight" in data:
        out["gross_weight"] = data["GrossWeight"]
    else:
        out["gross_weight"] = 0
    if "HazardousCargos" in data:
        import aws_sdk_geo_routes.types.route_hazardous_cargo_type_list

        out["hazardous_cargos"] = (
            aws_sdk_geo_routes.types.route_hazardous_cargo_type_list.deserialize_json(
                data["HazardousCargos"]
            )
        )
    if "Height" in data:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    if "HeightAboveFirstAxle" in data:
        out["height_above_first_axle"] = data["HeightAboveFirstAxle"]
    else:
        out["height_above_first_axle"] = 0
    if "KpraLength" in data:
        out["kpra_length"] = data["KpraLength"]
    else:
        out["kpra_length"] = 0
    if "Length" in data:
        out["length"] = data["Length"]
    else:
        out["length"] = 0
    if "LicensePlate" in data:
        import aws_sdk_geo_routes.types.route_vehicle_license_plate

        out["license_plate"] = (
            aws_sdk_geo_routes.types.route_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if "MaxSpeed" in data:
        out["max_speed"] = data["MaxSpeed"]
    if "Occupancy" in data:
        out["occupancy"] = data["Occupancy"]
    if "PayloadCapacity" in data:
        out["payload_capacity"] = data["PayloadCapacity"]
    else:
        out["payload_capacity"] = 0
    if "TireCount" in data:
        out["tire_count"] = data["TireCount"]
    if "Trailer" in data:
        import aws_sdk_geo_routes.types.route_trailer_options

        out["trailer"] = (
            aws_sdk_geo_routes.types.route_trailer_options.deserialize_json(
                data["Trailer"]
            )
        )
    if "TruckType" in data:
        import aws_sdk_geo_routes.types.route_truck_type

        out["truck_type"] = aws_sdk_geo_routes.types.route_truck_type.deserialize_json(
            data["TruckType"]
        )
    if "TunnelRestrictionCode" in data:
        out["tunnel_restriction_code"] = data["TunnelRestrictionCode"]
    if "WeightPerAxle" in data:
        out["weight_per_axle"] = data["WeightPerAxle"]
    else:
        out["weight_per_axle"] = 0
    if "WeightPerAxleGroup" in data:
        import aws_sdk_geo_routes.types.weight_per_axle_group

        out["weight_per_axle_group"] = (
            aws_sdk_geo_routes.types.weight_per_axle_group.deserialize_json(
                data["WeightPerAxleGroup"]
            )
        )
    if "Width" in data:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    return out
