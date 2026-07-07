"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNextDeparture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_transit_transport_mode_details
    import aws_sdk_geo_routes.types.route_transit_trip_status
    import aws_sdk_geo_routes.types.sensitive_string
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitNextDeparture(TypedDict, closed=True):
    delay: NotRequired["aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"]
    """<p>The delay from the scheduled departure time.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    platform_name: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Platform name or number for the departure.</p>"""
    status: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_trip_status.RouteTransitTripStatus"
    ]
    """<p>The status of the departure.</p>"""
    time: "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    """<p>The departure time.</p>"""
    transport: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_transport_mode_details.RouteTransitTransportModeDetails"
    ]
    """<p>Transport mode details for this departure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNextDeparture) -> dict:
    out: dict = {}
    if "delay" in value:
        out["Delay"] = value["delay"]
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "status" in value:
        import aws_sdk_geo_routes.types.route_transit_trip_status

        out["Status"] = (
            aws_sdk_geo_routes.types.route_transit_trip_status.serialize_json(
                value["status"]
            )
        )
    out["Time"] = value["time"]
    if "transport" in value:
        import aws_sdk_geo_routes.types.route_transit_transport_mode_details

        out["Transport"] = (
            aws_sdk_geo_routes.types.route_transit_transport_mode_details.serialize_json(
                value["transport"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitNextDeparture:
    out: RouteTransitNextDeparture = {}  # type: ignore[typeddict-item]
    if "Delay" in data:
        out["delay"] = data["Delay"]
    if "PlatformName" in data:
        out["platform_name"] = data["PlatformName"]
    if "Status" in data:
        import aws_sdk_geo_routes.types.route_transit_trip_status

        out["status"] = (
            aws_sdk_geo_routes.types.route_transit_trip_status.deserialize_json(
                data["Status"]
            )
        )
    if "Time" in data:
        out["time"] = data["Time"]
    else:
        raise DeserializationError("RouteTransitNextDeparture.time required")
    if "Transport" in data:
        import aws_sdk_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            aws_sdk_geo_routes.types.route_transit_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    return out
