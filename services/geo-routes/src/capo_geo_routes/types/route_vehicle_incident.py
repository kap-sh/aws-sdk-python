"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncident``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_incident_severity
    import capo_geo_routes.types.route_vehicle_incident_type
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteVehicleIncident(TypedDict, closed=True):
    description: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief readable description of the incident.</p>"""
    end_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>End timestamp of the incident.</p>"""
    severity: NotRequired[
        "capo_geo_routes.types.route_vehicle_incident_severity.RouteVehicleIncidentSeverity"
    ]
    """<p>Severity of the incident Critical - The part of the route the incident affects is unusable. Major- Major impact on the leg duration, for example stop and go Minor- Minor impact on the leg duration, for example traffic jam Low - Low on duration, for example slightly increased traffic</p>"""
    start_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Start time of the incident.</p>"""
    type: NotRequired[
        "capo_geo_routes.types.route_vehicle_incident_type.RouteVehicleIncidentType"
    ]
    """<p>Type of the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncident) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "severity" in value:
        import capo_geo_routes.types.route_vehicle_incident_severity

        out["Severity"] = (
            capo_geo_routes.types.route_vehicle_incident_severity.serialize_json(
                value["severity"]
            )
        )
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "type" in value:
        import capo_geo_routes.types.route_vehicle_incident_type

        out["Type"] = capo_geo_routes.types.route_vehicle_incident_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleIncident:
    out: RouteVehicleIncident = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "Severity" in data:
        import capo_geo_routes.types.route_vehicle_incident_severity

        out["severity"] = (
            capo_geo_routes.types.route_vehicle_incident_severity.deserialize_json(
                data["Severity"]
            )
        )
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "Type" in data:
        import capo_geo_routes.types.route_vehicle_incident_type

        out["type"] = (
            capo_geo_routes.types.route_vehicle_incident_type.deserialize_json(
                data["Type"]
            )
        )
    return out
