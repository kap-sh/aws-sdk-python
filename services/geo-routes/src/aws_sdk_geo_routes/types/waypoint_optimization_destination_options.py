"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationDestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.heading
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset
    import aws_sdk_geo_routes.types.waypoint_id
    import aws_sdk_geo_routes.types.waypoint_optimization_access_hours
    import aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options


class WaypointOptimizationDestinationOptions(TypedDict):
    access_hours: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_access_hours.WaypointOptimizationAccessHours"
    ]
    """<p>Access hours corresponding to when a waypoint can be visited.</p>"""
    appointment_time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Appointment time at the destination.</p>"""
    heading: "aws_sdk_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    id: NotRequired["aws_sdk_geo_routes.types.waypoint_id.WaypointId"]
    """<p>The waypoint Id.</p>"""
    service_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Service time spent at the destination. At an appointment, the service time should be the appointment duration.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    side_of_street: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options.WaypointOptimizationSideOfStreetOptions"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationDestinationOptions) -> dict:
    out: dict = {}
    if "access_hours" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_access_hours

        out["AccessHours"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_access_hours.serialize_json(
                value["access_hours"]
            )
        )
    if "appointment_time" in value:
        out["AppointmentTime"] = value["appointment_time"]
    out["Heading"] = value.get("heading", 0)
    if "id" in value:
        out["Id"] = value["id"]
    out["ServiceDuration"] = value.get("service_duration", 0)
    if "side_of_street" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options

        out["SideOfStreet"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationDestinationOptions:
    out: WaypointOptimizationDestinationOptions = {}  # type: ignore[typeddict-item]
    if "AccessHours" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_access_hours

        out["access_hours"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_access_hours.deserialize_json(
                data["AccessHours"]
            )
        )
    if "AppointmentTime" in data:
        out["appointment_time"] = data["AppointmentTime"]
    if "Heading" in data:
        out["heading"] = data["Heading"]
    else:
        out["heading"] = 0
    if "Id" in data:
        out["id"] = data["Id"]
    if "ServiceDuration" in data:
        out["service_duration"] = data["ServiceDuration"]
    else:
        out["service_duration"] = 0
    if "SideOfStreet" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options

        out["side_of_street"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out
