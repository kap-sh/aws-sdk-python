"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianLegDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list
    import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list
    import aws_sdk_geo_routes.types.route_pedestrian_arrival
    import aws_sdk_geo_routes.types.route_pedestrian_departure
    import aws_sdk_geo_routes.types.route_pedestrian_notice_list
    import aws_sdk_geo_routes.types.route_pedestrian_span_list
    import aws_sdk_geo_routes.types.route_pedestrian_summary
    import aws_sdk_geo_routes.types.route_pedestrian_travel_step_list


class RoutePedestrianLegDetails(TypedDict, closed=True):
    after_travel_steps: "aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list.RoutePedestrianAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "aws_sdk_geo_routes.types.route_pedestrian_arrival.RoutePedestrianArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    departure: (
        "aws_sdk_geo_routes.types.route_pedestrian_departure.RoutePedestrianDeparture"
    )
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: "aws_sdk_geo_routes.types.route_pedestrian_notice_list.RoutePedestrianNoticeList"
    r"""<p> Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    pass_through_waypoints: "aws_sdk_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    spans: "aws_sdk_geo_routes.types.route_pedestrian_span_list.RoutePedestrianSpanList"
    r"""<p> Spans that were computed for the requested SpanAdditionalFeatures. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    summary: NotRequired[
        "aws_sdk_geo_routes.types.route_pedestrian_summary.RoutePedestrianSummary"
    ]
    """<p>Summarized details of the leg.</p>"""
    travel_steps: "aws_sdk_geo_routes.types.route_pedestrian_travel_step_list.RoutePedestrianTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianLegDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list

    out["AfterTravelSteps"] = (
        aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list.serialize_json(
            value.get("after_travel_steps", [])
        )
    )
    import aws_sdk_geo_routes.types.route_pedestrian_arrival

    out["Arrival"] = aws_sdk_geo_routes.types.route_pedestrian_arrival.serialize_json(
        value["arrival"]
    )
    import aws_sdk_geo_routes.types.route_pedestrian_departure

    out["Departure"] = (
        aws_sdk_geo_routes.types.route_pedestrian_departure.serialize_json(
            value["departure"]
        )
    )
    import aws_sdk_geo_routes.types.route_pedestrian_notice_list

    out["Notices"] = (
        aws_sdk_geo_routes.types.route_pedestrian_notice_list.serialize_json(
            value["notices"]
        )
    )
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        aws_sdk_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    import aws_sdk_geo_routes.types.route_pedestrian_span_list

    out["Spans"] = aws_sdk_geo_routes.types.route_pedestrian_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_pedestrian_summary

        out["Summary"] = (
            aws_sdk_geo_routes.types.route_pedestrian_summary.serialize_json(
                value["summary"]
            )
        )
    import aws_sdk_geo_routes.types.route_pedestrian_travel_step_list

    out["TravelSteps"] = (
        aws_sdk_geo_routes.types.route_pedestrian_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RoutePedestrianLegDetails:
    out: RoutePedestrianLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list

        out["after_travel_steps"] = (
            aws_sdk_geo_routes.types.route_pedestrian_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if "Arrival" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_arrival

        out["arrival"] = (
            aws_sdk_geo_routes.types.route_pedestrian_arrival.deserialize_json(
                data["Arrival"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.arrival required")
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_pedestrian_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.departure required")
    if "Notices" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_notice_list

        out["notices"] = (
            aws_sdk_geo_routes.types.route_pedestrian_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.notices required")
    if "PassThroughWaypoints" in data:
        import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            aws_sdk_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "RoutePedestrianLegDetails.pass_through_waypoints required"
        )
    if "Spans" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_span_list

        out["spans"] = (
            aws_sdk_geo_routes.types.route_pedestrian_span_list.deserialize_json(
                data["Spans"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.spans required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_summary

        out["summary"] = (
            aws_sdk_geo_routes.types.route_pedestrian_summary.deserialize_json(
                data["Summary"]
            )
        )
    if "TravelSteps" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_travel_step_list

        out["travel_steps"] = (
            aws_sdk_geo_routes.types.route_pedestrian_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.travel_steps required")
    return out
