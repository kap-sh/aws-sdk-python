"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.position
    import aws_sdk_location.types.position_property_map
    import aws_sdk_location.types.positional_accuracy
    import aws_sdk_location.types.timestamp


class GetDevicePositionResponse(TypedDict):
    device_id: NotRequired["aws_sdk_location.types.id.Id"]
    """<p>The device whose position you retrieved.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp at which the device's position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    received_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the tracker resource received the device position. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    position: "aws_sdk_location.types.position.Position"
    """<p>The last known device position.</p>"""
    accuracy: NotRequired[
        "aws_sdk_location.types.positional_accuracy.PositionalAccuracy"
    ]
    """<p>The accuracy of the device position.</p>"""
    position_properties: NotRequired[
        "aws_sdk_location.types.position_property_map.PositionPropertyMap"
    ]
    """<p>The properties associated with the position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.timestamp

    out["SampleTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import aws_sdk_location.types.timestamp

    out["ReceivedTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["received_time"]
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


def deserialize_json(data: dict) -> GetDevicePositionResponse:
    out: GetDevicePositionResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("GetDevicePositionResponse.sample_time required")
    if "ReceivedTime" in data:
        import aws_sdk_location.types.timestamp

        out["received_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["ReceivedTime"]
        )
    else:
        raise DeserializationError("GetDevicePositionResponse.received_time required")
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("GetDevicePositionResponse.position required")
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
