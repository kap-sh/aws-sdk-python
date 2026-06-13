"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_item_error
    import aws_sdk_location.types.id


class BatchGetDevicePositionError(TypedDict):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The ID of the device that didn't return a position.</p>"""
    error: "aws_sdk_location.types.batch_item_error.BatchItemError"
    """<p>Contains details related to the error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.batch_item_error

    out["Error"] = aws_sdk_location.types.batch_item_error.serialize_json(
        value["error"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetDevicePositionError:
    out: BatchGetDevicePositionError = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("BatchGetDevicePositionError.device_id required")
    if "Error" in data:
        import aws_sdk_location.types.batch_item_error

        out["error"] = aws_sdk_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchGetDevicePositionError.error required")
    return out
