"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_avoidance_area_list
    import aws_sdk_geo_routes.types.route_avoidance_zone_category_list
    import aws_sdk_geo_routes.types.sensitive_boolean
    import aws_sdk_geo_routes.types.truck_road_type_list


class RouteAvoidanceOptions(TypedDict):
    areas: NotRequired[
        "aws_sdk_geo_routes.types.route_avoidance_area_list.RouteAvoidanceAreaList"
    ]
    r"""<p> Areas to be avoided. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    car_shuttle_trains: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Avoid car-shuttle-trains while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    controlled_access_highways: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid controlled access highways while calculating the route.</p>"""
    dirt_roads: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Avoid dirt roads while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    ferries: NotRequired["aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoid ferries while calculating the route.</p>"""
    seasonal_closure: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Avoid roads that have seasonal closure while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    toll_roads: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoids roads where the specified toll transponders are the only mode of payment.</p>"""
    toll_transponders: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Avoids roads where the specified toll transponders are the only mode of payment. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    truck_road_types: NotRequired[
        "aws_sdk_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    ]
    r"""<p> Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    tunnels: NotRequired["aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    r"""<p> Avoid tunnels while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    u_turns: NotRequired["aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    r"""<p> Avoid U-turns for calculation on highways and motorways. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    zone_categories: NotRequired[
        "aws_sdk_geo_routes.types.route_avoidance_zone_category_list.RouteAvoidanceZoneCategoryList"
    ]
    r"""<p> Zone categories to be avoided. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceOptions) -> dict:
    out: dict = {}
    if "areas" in value:
        import aws_sdk_geo_routes.types.route_avoidance_area_list

        out["Areas"] = (
            aws_sdk_geo_routes.types.route_avoidance_area_list.serialize_json(
                value["areas"]
            )
        )
    if "car_shuttle_trains" in value:
        out["CarShuttleTrains"] = value["car_shuttle_trains"]
    if "controlled_access_highways" in value:
        out["ControlledAccessHighways"] = value["controlled_access_highways"]
    if "dirt_roads" in value:
        out["DirtRoads"] = value["dirt_roads"]
    if "ferries" in value:
        out["Ferries"] = value["ferries"]
    if "seasonal_closure" in value:
        out["SeasonalClosure"] = value["seasonal_closure"]
    if "toll_roads" in value:
        out["TollRoads"] = value["toll_roads"]
    if "toll_transponders" in value:
        out["TollTransponders"] = value["toll_transponders"]
    if "truck_road_types" in value:
        import aws_sdk_geo_routes.types.truck_road_type_list

        out["TruckRoadTypes"] = (
            aws_sdk_geo_routes.types.truck_road_type_list.serialize_json(
                value["truck_road_types"]
            )
        )
    if "tunnels" in value:
        out["Tunnels"] = value["tunnels"]
    if "u_turns" in value:
        out["UTurns"] = value["u_turns"]
    if "zone_categories" in value:
        import aws_sdk_geo_routes.types.route_avoidance_zone_category_list

        out["ZoneCategories"] = (
            aws_sdk_geo_routes.types.route_avoidance_zone_category_list.serialize_json(
                value["zone_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAvoidanceOptions:
    out: RouteAvoidanceOptions = {}  # type: ignore[typeddict-item]
    if "Areas" in data:
        import aws_sdk_geo_routes.types.route_avoidance_area_list

        out["areas"] = (
            aws_sdk_geo_routes.types.route_avoidance_area_list.deserialize_json(
                data["Areas"]
            )
        )
    if "CarShuttleTrains" in data:
        out["car_shuttle_trains"] = data["CarShuttleTrains"]
    if "ControlledAccessHighways" in data:
        out["controlled_access_highways"] = data["ControlledAccessHighways"]
    if "DirtRoads" in data:
        out["dirt_roads"] = data["DirtRoads"]
    if "Ferries" in data:
        out["ferries"] = data["Ferries"]
    if "SeasonalClosure" in data:
        out["seasonal_closure"] = data["SeasonalClosure"]
    if "TollRoads" in data:
        out["toll_roads"] = data["TollRoads"]
    if "TollTransponders" in data:
        out["toll_transponders"] = data["TollTransponders"]
    if "TruckRoadTypes" in data:
        import aws_sdk_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            aws_sdk_geo_routes.types.truck_road_type_list.deserialize_json(
                data["TruckRoadTypes"]
            )
        )
    if "Tunnels" in data:
        out["tunnels"] = data["Tunnels"]
    if "UTurns" in data:
        out["u_turns"] = data["UTurns"]
    if "ZoneCategories" in data:
        import aws_sdk_geo_routes.types.route_avoidance_zone_category_list

        out["zone_categories"] = (
            aws_sdk_geo_routes.types.route_avoidance_zone_category_list.deserialize_json(
                data["ZoneCategories"]
            )
        )
    return out
