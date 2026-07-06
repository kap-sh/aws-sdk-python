"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_item_error
    import aws_sdk_location.types.id


class BatchDeleteDevicePositionHistoryError(TypedDict, closed=True):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The ID of the device for this position.</p>"""
    error: "aws_sdk_location.types.batch_item_error.BatchItemError"


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.batch_item_error

    out["Error"] = aws_sdk_location.types.batch_item_error.serialize_json(
        value["error"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDevicePositionHistoryError:
    out: BatchDeleteDevicePositionHistoryError = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "BatchDeleteDevicePositionHistoryError.device_id required"
        )
    if "Error" in data:
        import aws_sdk_location.types.batch_item_error

        out["error"] = aws_sdk_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError(
            "BatchDeleteDevicePositionHistoryError.error required"
        )
    return out
