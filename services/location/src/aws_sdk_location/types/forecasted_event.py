"""Generated from Smithy shape ``com.amazonaws.location#ForecastedEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.forecasted_geofence_event_type
    import aws_sdk_location.types.id
    import aws_sdk_location.types.nearest_distance
    import aws_sdk_location.types.property_map
    import aws_sdk_location.types.timestamp
    import aws_sdk_location.types.uuid


class ForecastedEvent(TypedDict):
    event_id: "aws_sdk_location.types.uuid.Uuid"
    """<p>The forecasted event identifier.</p>"""
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence identifier pertaining to the forecasted event.</p>"""
    is_device_in_geofence: "bool"
    """<p>Indicates if the device is located within the geofence.</p>"""
    nearest_distance: "aws_sdk_location.types.nearest_distance.NearestDistance"
    """<p>The closest distance from the device's position to the geofence.</p>"""
    event_type: "aws_sdk_location.types.forecasted_geofence_event_type.ForecastedGeofenceEventType"
    """<p>The event type, forecasting three states for which a device can be in relative to a geofence:</p> <p> <code>ENTER</code>: If a device is outside of a geofence, but would breach the fence if the device is moving at its current speed within time horizon window.</p> <p> <code>EXIT</code>: If a device is inside of a geofence, but would breach the fence if the device is moving at its current speed within time horizon window.</p> <p> <code>IDLE</code>: If a device is inside of a geofence, and the device is not moving.</p>"""
    forecasted_breach_time: NotRequired["aws_sdk_location.types.timestamp.Timestamp"]
    r"""<p>The forecasted time the device will breach the geofence in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    geofence_properties: NotRequired["aws_sdk_location.types.property_map.PropertyMap"]
    """<p>The geofence properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastedEvent) -> dict:
    out: dict = {}
    out["EventId"] = value["event_id"]
    out["GeofenceId"] = value["geofence_id"]
    out["IsDeviceInGeofence"] = value["is_device_in_geofence"]
    out["NearestDistance"] = value.get("nearest_distance", 0)
    out["EventType"] = value["event_type"]
    if "forecasted_breach_time" in value:
        import aws_sdk_location.types.timestamp

        out["ForecastedBreachTime"] = aws_sdk_location.types.timestamp.serialize_json(
            value["forecasted_breach_time"]
        )
    if "geofence_properties" in value:
        import aws_sdk_location.types.property_map

        out["GeofenceProperties"] = aws_sdk_location.types.property_map.serialize_json(
            value["geofence_properties"]
        )
    return out


def deserialize_json(data: dict) -> ForecastedEvent:
    out: ForecastedEvent = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("ForecastedEvent.event_id required")
    if "GeofenceId" in data:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("ForecastedEvent.geofence_id required")
    if "IsDeviceInGeofence" in data:
        out["is_device_in_geofence"] = data["IsDeviceInGeofence"]
    else:
        raise DeserializationError("ForecastedEvent.is_device_in_geofence required")
    if "NearestDistance" in data:
        out["nearest_distance"] = data["NearestDistance"]
    else:
        out["nearest_distance"] = 0
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    else:
        raise DeserializationError("ForecastedEvent.event_type required")
    if "ForecastedBreachTime" in data:
        import aws_sdk_location.types.timestamp

        out["forecasted_breach_time"] = (
            aws_sdk_location.types.timestamp.deserialize_json(
                data["ForecastedBreachTime"]
            )
        )
    if "GeofenceProperties" in data:
        import aws_sdk_location.types.property_map

        out["geofence_properties"] = (
            aws_sdk_location.types.property_map.deserialize_json(
                data["GeofenceProperties"]
            )
        )
    return out
