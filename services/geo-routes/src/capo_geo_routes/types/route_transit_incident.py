"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncident``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_incident_effect
    import capo_geo_routes.types.route_transit_incident_type
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitIncident(TypedDict, closed=True):
    description: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>A human readable description of the incident.</p>"""
    effect: (
        "capo_geo_routes.types.route_transit_incident_effect.RouteTransitIncidentEffect"
    )
    """<p>The effect of the incident on the transit service.</p>"""
    end_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The end time of the incident.</p>"""
    start_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The start time of the incident.</p>"""
    type: "capo_geo_routes.types.route_transit_incident_type.RouteTransitIncidentType"
    """<p>Type of the incident.</p>"""
    url: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>URL to the original incident published at the agency website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncident) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_geo_routes.types.route_transit_incident_effect

    out["Effect"] = capo_geo_routes.types.route_transit_incident_effect.serialize_json(
        value["effect"]
    )
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    import capo_geo_routes.types.route_transit_incident_type

    out["Type"] = capo_geo_routes.types.route_transit_incident_type.serialize_json(
        value["type"]
    )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteTransitIncident:
    out: RouteTransitIncident = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Effect" in data:
        import capo_geo_routes.types.route_transit_incident_effect

        out["effect"] = (
            capo_geo_routes.types.route_transit_incident_effect.deserialize_json(
                data["Effect"]
            )
        )
    else:
        raise DeserializationError("RouteTransitIncident.effect required")
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "Type" in data:
        import capo_geo_routes.types.route_transit_incident_type

        out["type"] = (
            capo_geo_routes.types.route_transit_incident_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTransitIncident.type required")
    if "Url" in data:
        out["url"] = data["Url"]
    return out
