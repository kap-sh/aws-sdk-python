"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_area_list
    import capo_geo_routes.types.isoline_avoidance_zone_category_list
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.truck_road_type_list


class IsolineAvoidanceOptions(TypedDict, closed=True):
    areas: NotRequired[
        "capo_geo_routes.types.isoline_avoidance_area_list.IsolineAvoidanceAreaList"
    ]
    """<p>Specifies geographic areas to avoid where possible. Routes may still pass through these areas if no reasonable alternative exists.</p>"""
    car_shuttle_trains: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid car shuttle trains (auto trains) where possible. These may still be included if no reasonable alternative route exists.</p>"""
    controlled_access_highways: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid controlled-access highways (such as interstate highways or motorways) where possible. If a viable route cannot be calculated using only local roads, controlled-access highways may still be included.</p>"""
    dirt_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid unpaved or dirt roads where possible. Routes may still include dirt roads if no reasonable paved alternative exists.</p>"""
    ferries: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid ferries where possible. If a viable route cannot be calculated without using ferries, they may still be included.</p>"""
    seasonal_closure: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid roads that may be subject to seasonal closures where possible. These roads may still be included if no reasonable year-round alternative exists.</p>"""
    toll_roads: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid toll roads where possible. If a viable route cannot be calculated without using toll roads, they may still be included.</p>"""
    toll_transponders: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Indicates a preference to avoid roads that require electronic toll collection transponders where possible. These roads may still be included if no viable alternative route exists.</p>"""
    truck_road_types: NotRequired[
        "capo_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    ]
    """<p>For truck travel modes, indicates specific road classification types in Sweden (<code> BK1</code> through <code>BK4</code>) and Mexico (<code>A2, A4, B2, B4, C, D, ET2, ET4</code>) to avoid where possible. These road types may still be used if no reasonable alternative exists.</p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    tunnels: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid tunnels where possible. If a viable route cannot be calculated without using tunnels, they may still be included.</p>"""
    u_turns: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Indicates a preference to avoid U-turns where possible. U-turns may still be included if necessary to reach certain areas or when no reasonable alternative exists.</p>"""
    zone_categories: NotRequired[
        "capo_geo_routes.types.isoline_avoidance_zone_category_list.IsolineAvoidanceZoneCategoryList"
    ]
    """<p>Indicates types of regulated zones (such as congestion pricing or environmental zones) to avoid where possible. Routes may still pass through these zones if no reasonable alternative exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceOptions) -> dict:
    out: dict = {}
    if "areas" in value:
        import capo_geo_routes.types.isoline_avoidance_area_list

        out["Areas"] = capo_geo_routes.types.isoline_avoidance_area_list.serialize_json(
            value["areas"]
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
        import capo_geo_routes.types.truck_road_type_list

        out["TruckRoadTypes"] = (
            capo_geo_routes.types.truck_road_type_list.serialize_json(
                value["truck_road_types"]
            )
        )
    if "tunnels" in value:
        out["Tunnels"] = value["tunnels"]
    if "u_turns" in value:
        out["UTurns"] = value["u_turns"]
    if "zone_categories" in value:
        import capo_geo_routes.types.isoline_avoidance_zone_category_list

        out["ZoneCategories"] = (
            capo_geo_routes.types.isoline_avoidance_zone_category_list.serialize_json(
                value["zone_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> IsolineAvoidanceOptions:
    out: IsolineAvoidanceOptions = {}  # type: ignore[typeddict-item]
    if "Areas" in data:
        import capo_geo_routes.types.isoline_avoidance_area_list

        out["areas"] = (
            capo_geo_routes.types.isoline_avoidance_area_list.deserialize_json(
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
        import capo_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            capo_geo_routes.types.truck_road_type_list.deserialize_json(
                data["TruckRoadTypes"]
            )
        )
    if "Tunnels" in data:
        out["tunnels"] = data["Tunnels"]
    if "UTurns" in data:
        out["u_turns"] = data["UTurns"]
    if "ZoneCategories" in data:
        import capo_geo_routes.types.isoline_avoidance_zone_category_list

        out["zone_categories"] = (
            capo_geo_routes.types.isoline_avoidance_zone_category_list.deserialize_json(
                data["ZoneCategories"]
            )
        )
    return out
