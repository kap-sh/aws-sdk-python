"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_update_device_position_error_list


class BatchUpdateDevicePositionResponse(TypedDict):
    errors: "aws_sdk_location.types.batch_update_device_position_error_list.BatchUpdateDevicePositionErrorList"
    """<p>Contains error details for each device that failed to update its position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.batch_update_device_position_error_list

    out["Errors"] = (
        aws_sdk_location.types.batch_update_device_position_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDevicePositionResponse:
    out: BatchUpdateDevicePositionResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_location.types.batch_update_device_position_error_list

        out["errors"] = (
            aws_sdk_location.types.batch_update_device_position_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateDevicePositionResponse.errors required")
    return out
