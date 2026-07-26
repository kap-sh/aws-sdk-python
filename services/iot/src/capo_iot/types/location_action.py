"""Generated from Smithy shape ``com.amazonaws.iot#LocationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.location_timestamp
    import capo_iot.types.string


class LocationAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that grants permission to write to the Amazon Location resource.</p>"""
    tracker_name: "capo_iot.types.string.String"
    """<p>The name of the tracker resource in Amazon Location in which the location is updated.</p>"""
    device_id: "capo_iot.types.string.String"
    """<p>The unique ID of the device providing the location data.</p>"""
    timestamp: NotRequired["capo_iot.types.location_timestamp.LocationTimestamp"]
    """<p>The time that the location data was sampled. The default value is the time the MQTT message was processed.</p>"""
    latitude: "capo_iot.types.string.String"
    """<p>A string that evaluates to a double value that represents the latitude of the device's location.</p>"""
    longitude: "capo_iot.types.string.String"
    """<p>A string that evaluates to a double value that represents the longitude of the device's location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["trackerName"] = value["tracker_name"]
    out["deviceId"] = value["device_id"]
    if "timestamp" in value:
        import capo_iot.types.location_timestamp

        out["timestamp"] = capo_iot.types.location_timestamp.serialize_json(
            value["timestamp"]
        )
    out["latitude"] = value["latitude"]
    out["longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> LocationAction:
    out: LocationAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("LocationAction.role_arn required")
    if "trackerName" in data:
        out["tracker_name"] = data["trackerName"]
    else:
        raise DeserializationError("LocationAction.tracker_name required")
    if "deviceId" in data:
        out["device_id"] = data["deviceId"]
    else:
        raise DeserializationError("LocationAction.device_id required")
    if "timestamp" in data:
        import capo_iot.types.location_timestamp

        out["timestamp"] = capo_iot.types.location_timestamp.deserialize_json(
            data["timestamp"]
        )
    if "latitude" in data:
        out["latitude"] = data["latitude"]
    else:
        raise DeserializationError("LocationAction.latitude required")
    if "longitude" in data:
        out["longitude"] = data["longitude"]
    else:
        raise DeserializationError("LocationAction.longitude required")
    return out
