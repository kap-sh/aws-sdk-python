"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_item_error
    import aws_sdk_location.types.id
    import aws_sdk_location.types.timestamp


class BatchUpdateDevicePositionError(TypedDict):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The device associated with the failed location update.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    error: "aws_sdk_location.types.batch_item_error.BatchItemError"
    """<p>Contains details related to the error code such as the error code and error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.timestamp

    out["SampleTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import aws_sdk_location.types.batch_item_error

    out["Error"] = aws_sdk_location.types.batch_item_error.serialize_json(
        value["error"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDevicePositionError:
    out: BatchUpdateDevicePositionError = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("BatchUpdateDevicePositionError.device_id required")
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError(
            "BatchUpdateDevicePositionError.sample_time required"
        )
    if "Error" in data:
        import aws_sdk_location.types.batch_item_error

        out["error"] = aws_sdk_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchUpdateDevicePositionError.error required")
    return out
