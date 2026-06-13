"""Generated from Smithy shape ``com.amazonaws.location#ListDevicePositionsResponseEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.position
    import aws_sdk_location.types.position_property_map
    import aws_sdk_location.types.positional_accuracy
    import aws_sdk_location.types.timestamp


class ListDevicePositionsResponseEntry(TypedDict):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The ID of the device for this position.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    position: "aws_sdk_location.types.position.Position"
    """<p>The last known device position. Empty if no positions currently stored.</p>"""
    accuracy: NotRequired[
        "aws_sdk_location.types.positional_accuracy.PositionalAccuracy"
    ]
    """<p>The accuracy of the device position.</p>"""
    position_properties: NotRequired[
        "aws_sdk_location.types.position_property_map.PositionPropertyMap"
    ]
    """<p>The properties associated with the position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicePositionsResponseEntry) -> dict:
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


def deserialize_json(data: dict) -> ListDevicePositionsResponseEntry:
    out: ListDevicePositionsResponseEntry = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "ListDevicePositionsResponseEntry.device_id required"
        )
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError(
            "ListDevicePositionsResponseEntry.sample_time required"
        )
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("ListDevicePositionsResponseEntry.position required")
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
