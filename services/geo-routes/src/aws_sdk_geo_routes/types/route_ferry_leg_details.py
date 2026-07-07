"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryLegDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_after_travel_step_list
    import aws_sdk_geo_routes.types.route_ferry_arrival
    import aws_sdk_geo_routes.types.route_ferry_before_travel_step_list
    import aws_sdk_geo_routes.types.route_ferry_departure
    import aws_sdk_geo_routes.types.route_ferry_notice_list
    import aws_sdk_geo_routes.types.route_ferry_span_list
    import aws_sdk_geo_routes.types.route_ferry_summary
    import aws_sdk_geo_routes.types.route_ferry_travel_step_list
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list
    import aws_sdk_geo_routes.types.sensitive_string


class RouteFerryLegDetails(TypedDict, closed=True):
    after_travel_steps: "aws_sdk_geo_routes.types.route_ferry_after_travel_step_list.RouteFerryAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "aws_sdk_geo_routes.types.route_ferry_arrival.RouteFerryArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    before_travel_steps: "aws_sdk_geo_routes.types.route_ferry_before_travel_step_list.RouteFerryBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    departure: "aws_sdk_geo_routes.types.route_ferry_departure.RouteFerryDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: "aws_sdk_geo_routes.types.route_ferry_notice_list.RouteFerryNoticeList"
    """<p>Notices are additional information returned that indicate issues that occurred during route calculation.</p>"""
    pass_through_waypoints: "aws_sdk_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    route_name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Route name of the ferry line.</p>"""
    spans: "aws_sdk_geo_routes.types.route_ferry_span_list.RouteFerrySpanList"
    """<p>Spans that were computed for the requested SpanAdditionalFeatures.</p>"""
    summary: NotRequired[
        "aws_sdk_geo_routes.types.route_ferry_summary.RouteFerrySummary"
    ]
    """<p>Summarized details of the leg.</p>"""
    travel_steps: (
        "aws_sdk_geo_routes.types.route_ferry_travel_step_list.RouteFerryTravelStepList"
    )
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryLegDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_ferry_after_travel_step_list

    out["AfterTravelSteps"] = (
        aws_sdk_geo_routes.types.route_ferry_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_ferry_arrival

    out["Arrival"] = aws_sdk_geo_routes.types.route_ferry_arrival.serialize_json(
        value["arrival"]
    )
    import aws_sdk_geo_routes.types.route_ferry_before_travel_step_list

    out["BeforeTravelSteps"] = (
        aws_sdk_geo_routes.types.route_ferry_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_ferry_departure

    out["Departure"] = aws_sdk_geo_routes.types.route_ferry_departure.serialize_json(
        value["departure"]
    )
    import aws_sdk_geo_routes.types.route_ferry_notice_list

    out["Notices"] = aws_sdk_geo_routes.types.route_ferry_notice_list.serialize_json(
        value["notices"]
    )
    import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        aws_sdk_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    if "route_name" in value:
        out["RouteName"] = value["route_name"]
    import aws_sdk_geo_routes.types.route_ferry_span_list

    out["Spans"] = aws_sdk_geo_routes.types.route_ferry_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_ferry_summary

        out["Summary"] = aws_sdk_geo_routes.types.route_ferry_summary.serialize_json(
            value["summary"]
        )
    import aws_sdk_geo_routes.types.route_ferry_travel_step_list

    out["TravelSteps"] = (
        aws_sdk_geo_routes.types.route_ferry_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteFerryLegDetails:
    out: RouteFerryLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_ferry_after_travel_step_list

        out["after_travel_steps"] = (
            aws_sdk_geo_routes.types.route_ferry_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.after_travel_steps required")
    if "Arrival" in data:
        import aws_sdk_geo_routes.types.route_ferry_arrival

        out["arrival"] = aws_sdk_geo_routes.types.route_ferry_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.arrival required")
    if "BeforeTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_ferry_before_travel_step_list

        out["before_travel_steps"] = (
            aws_sdk_geo_routes.types.route_ferry_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.before_travel_steps required")
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_ferry_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_ferry_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.departure required")
    if "Notices" in data:
        import aws_sdk_geo_routes.types.route_ferry_notice_list

        out["notices"] = (
            aws_sdk_geo_routes.types.route_ferry_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.notices required")
    if "PassThroughWaypoints" in data:
        import aws_sdk_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            aws_sdk_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "RouteFerryLegDetails.pass_through_waypoints required"
        )
    if "RouteName" in data:
        out["route_name"] = data["RouteName"]
    if "Spans" in data:
        import aws_sdk_geo_routes.types.route_ferry_span_list

        out["spans"] = aws_sdk_geo_routes.types.route_ferry_span_list.deserialize_json(
            data["Spans"]
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.spans required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_ferry_summary

        out["summary"] = aws_sdk_geo_routes.types.route_ferry_summary.deserialize_json(
            data["Summary"]
        )
    if "TravelSteps" in data:
        import aws_sdk_geo_routes.types.route_ferry_travel_step_list

        out["travel_steps"] = (
            aws_sdk_geo_routes.types.route_ferry_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.travel_steps required")
    return out
