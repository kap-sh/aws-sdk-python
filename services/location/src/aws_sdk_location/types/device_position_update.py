"""Generated from Smithy shape ``com.amazonaws.location#DevicePositionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.position
    import aws_sdk_location.types.position_property_map
    import aws_sdk_location.types.positional_accuracy
    import aws_sdk_location.types.timestamp


class DevicePositionUpdate(TypedDict, closed=True):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The device associated to the position update.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp at which the device's position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    position: "aws_sdk_location.types.position.Position"
    r"""<p>The latest device position defined in <a href=\"https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84\">WGS 84</a> format: <code>[X or longitude, Y or latitude]</code>.</p>"""
    accuracy: NotRequired[
        "aws_sdk_location.types.positional_accuracy.PositionalAccuracy"
    ]
    """<p>The accuracy of the device position.</p>"""
    position_properties: NotRequired[
        "aws_sdk_location.types.position_property_map.PositionPropertyMap"
    ]
    r"""<p>Associates one of more properties with the position update. A property is a key-value pair stored with the position update and added to any geofence event the update may trigger.</p> <p>Format: <code>\"key\" : \"value\"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevicePositionUpdate) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.timestamp

    out["SampleTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import aws_sdk_location.types.position

    out["Position"] = aws_sdk_location.types.position.serialize_json(value["position"])
    if "accuracy" in value:
        import aws_sdk_location.types.positional_accuracy

        out["Accuracy"] = aws_sdk_location.types.positional_accuracy.serialize_json(
            value["accuracy"]
        )
    if "position_properties" in value:
        import aws_sdk_location.types.position_property_map

        out["PositionProperties"] = (
            aws_sdk_location.types.position_property_map.serialize_json(
                value["position_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> DevicePositionUpdate:
    out: DevicePositionUpdate = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("DevicePositionUpdate.device_id required")
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("DevicePositionUpdate.sample_time required")
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("DevicePositionUpdate.position required")
    if "Accuracy" in data:
        import aws_sdk_location.types.positional_accuracy

        out["accuracy"] = aws_sdk_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if "PositionProperties" in data:
        import aws_sdk_location.types.position_property_map

        out["position_properties"] = (
            aws_sdk_location.types.position_property_map.deserialize_json(
                data["PositionProperties"]
            )
        )
    return out
