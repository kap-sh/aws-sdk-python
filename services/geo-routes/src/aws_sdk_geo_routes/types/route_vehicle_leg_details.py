"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleLegDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list
    import aws_sdk_geo_routes.types.route_toll_list
    import aws_sdk_geo_routes.types.route_toll_system_list
    import aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list
    import aws_sdk_geo_routes.types.route_vehicle_arrival
    import aws_sdk_geo_routes.types.route_vehicle_departure
    import aws_sdk_geo_routes.types.route_vehicle_incident_list
    import aws_sdk_geo_routes.types.route_vehicle_notice_list
    import aws_sdk_geo_routes.types.route_vehicle_span_list
    import aws_sdk_geo_routes.types.route_vehicle_summary
    import aws_sdk_geo_routes.types.route_vehicle_travel_step_list
    import aws_sdk_geo_routes.types.route_zone_list
    import aws_sdk_geo_routes.types.truck_road_type_list


class RouteVehicleLegDetails(TypedDict):
    after_travel_steps: "aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list.RouteVehicleAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "aws_sdk_geo_routes.types.route_vehicle_arrival.RouteVehicleArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    departure: "aws_sdk_geo_routes.types.route_vehicle_departure.RouteVehicleDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    incidents: (
        "aws_sdk_geo_routes.types.route_vehicle_incident_list.RouteVehicleIncidentList"
    )
    """<p> Incidents corresponding to this leg of the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    notices: "aws_sdk_geo_routes.types.route_vehicle_notice_list.RouteVehicleNoticeList"
    """<p> Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    pass_through_waypoints: "aws_sdk_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    spans: "aws_sdk_geo_routes.types.route_vehicle_span_list.RouteVehicleSpanList"
    """<p> Spans that were computed for the requested SpanAdditionalFeatures. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    summary: NotRequired[
        "aws_sdk_geo_routes.types.route_vehicle_summary.RouteVehicleSummary"
    ]
    """<p>Summarized details of the leg.</p>"""
    tolls: "aws_sdk_geo_routes.types.route_toll_list.RouteTollList"
    """<p> Toll related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    toll_systems: "aws_sdk_geo_routes.types.route_toll_system_list.RouteTollSystemList"
    """<p> Toll systems are authorities that collect payments for the toll. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    travel_steps: "aws_sdk_geo_routes.types.route_vehicle_travel_step_list.RouteVehicleTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    truck_road_types: "aws_sdk_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    """<p> Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    zones: "aws_sdk_geo_routes.types.route_zone_list.RouteZoneList"
    """<p> Zones corresponding to this leg of the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleLegDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list

    out["AfterTravelSteps"] = (
        aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list.serialize_json(
            value.get("after_travel_steps", [])
        )
    )
    import aws_sdk_geo_routes.types.route_vehicle_arrival

    out["Arrival"] = aws_sdk_geo_routes.types.route_vehicle_arrival.serialize_json(
        value["arrival"]
    )
    import aws_sdk_geo_routes.types.route_vehicle_departure

    out["Departure"] = aws_sdk_geo_routes.types.route_vehicle_departure.serialize_json(
        value["departure"]
    )
    import aws_sdk_geo_routes.types.route_vehicle_incident_list

    out["Incidents"] = (
        aws_sdk_geo_routes.types.route_vehicle_incident_list.serialize_json(
            value["incidents"]
        )
    )
    import aws_sdk_geo_routes.types.route_vehicle_notice_list

    out["Notices"] = aws_sdk_geo_routes.types.route_vehicle_notice_list.serialize_json(
        value["notices"]
    )
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        aws_sdk_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    import aws_sdk_geo_routes.types.route_vehicle_span_list

    out["Spans"] = aws_sdk_geo_routes.types.route_vehicle_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_vehicle_summary

        out["Summary"] = aws_sdk_geo_routes.types.route_vehicle_summary.serialize_json(
            value["summary"]
        )
    import aws_sdk_geo_routes.types.route_toll_list

    out["Tolls"] = aws_sdk_geo_routes.types.route_toll_list.serialize_json(
        value["tolls"]
    )
    import aws_sdk_geo_routes.types.route_toll_system_list

    out["TollSystems"] = aws_sdk_geo_routes.types.route_toll_system_list.serialize_json(
        value["toll_systems"]
    )
    import aws_sdk_geo_routes.types.route_vehicle_travel_step_list

    out["TravelSteps"] = (
        aws_sdk_geo_routes.types.route_vehicle_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.truck_road_type_list

    out["TruckRoadTypes"] = (
        aws_sdk_geo_routes.types.truck_road_type_list.serialize_json(
            value["truck_road_types"]
        )
    )
    import aws_sdk_geo_routes.types.route_zone_list

    out["Zones"] = aws_sdk_geo_routes.types.route_zone_list.serialize_json(
        value["zones"]
    )
    return out


def deserialize_json(data: dict) -> RouteVehicleLegDetails:
    out: RouteVehicleLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list

        out["after_travel_steps"] = (
            aws_sdk_geo_routes.types.route_vehicle_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if "Arrival" in data:
        import aws_sdk_geo_routes.types.route_vehicle_arrival

        out["arrival"] = (
            aws_sdk_geo_routes.types.route_vehicle_arrival.deserialize_json(
                data["Arrival"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.arrival required")
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_vehicle_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_vehicle_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.departure required")
    if "Incidents" in data:
        import aws_sdk_geo_routes.types.route_vehicle_incident_list

        out["incidents"] = (
            aws_sdk_geo_routes.types.route_vehicle_incident_list.deserialize_json(
                data["Incidents"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.incidents required")
    if "Notices" in data:
        import aws_sdk_geo_routes.types.route_vehicle_notice_list

        out["notices"] = (
            aws_sdk_geo_routes.types.route_vehicle_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.notices required")
    if "PassThroughWaypoints" in data:
        import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            aws_sdk_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "RouteVehicleLegDetails.pass_through_waypoints required"
        )
    if "Spans" in data:
        import aws_sdk_geo_routes.types.route_vehicle_span_list

        out["spans"] = (
            aws_sdk_geo_routes.types.route_vehicle_span_list.deserialize_json(
                data["Spans"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.spans required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_vehicle_summary

        out["summary"] = (
            aws_sdk_geo_routes.types.route_vehicle_summary.deserialize_json(
                data["Summary"]
            )
        )
    if "Tolls" in data:
        import aws_sdk_geo_routes.types.route_toll_list

        out["tolls"] = aws_sdk_geo_routes.types.route_toll_list.deserialize_json(
            data["Tolls"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.tolls required")
    if "TollSystems" in data:
        import aws_sdk_geo_routes.types.route_toll_system_list

        out["toll_systems"] = (
            aws_sdk_geo_routes.types.route_toll_system_list.deserialize_json(
                data["TollSystems"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.toll_systems required")
    if "TravelSteps" in data:
        import aws_sdk_geo_routes.types.route_vehicle_travel_step_list

        out["travel_steps"] = (
            aws_sdk_geo_routes.types.route_vehicle_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.travel_steps required")
    if "TruckRoadTypes" in data:
        import aws_sdk_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            aws_sdk_geo_routes.types.truck_road_type_list.deserialize_json(
                data["TruckRoadTypes"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.truck_road_types required")
    if "Zones" in data:
        import aws_sdk_geo_routes.types.route_zone_list

        out["zones"] = aws_sdk_geo_routes.types.route_zone_list.deserialize_json(
            data["Zones"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.zones required")
    return out
