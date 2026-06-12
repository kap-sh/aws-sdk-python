"""Generated from Smithy shape ``com.amazonaws.wickr#BatchResetDevicesForUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_device_error_response_items
    import aws_sdk_wickr.types.batch_device_success_response_items
    import aws_sdk_wickr.types.generic_string


class BatchResetDevicesForUserResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch device reset operation.</p>"""
    successful: NotRequired[
        "aws_sdk_wickr.types.batch_device_success_response_items.BatchDeviceSuccessResponseItems"
    ]
    """<p>A list of application IDs that were successfully reset.</p>"""
    failed: NotRequired[
        "aws_sdk_wickr.types.batch_device_error_response_items.BatchDeviceErrorResponseItems"
    ]
    """<p>A list of device reset attempts that failed, including error details explaining why each device could not be reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchResetDevicesForUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import aws_sdk_wickr.types.batch_device_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_device_success_response_items.serialize_json(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_wickr.types.batch_device_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_device_error_response_items.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchResetDevicesForUserResponse:
    out: BatchResetDevicesForUserResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "successful" in data:
        import aws_sdk_wickr.types.batch_device_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_device_success_response_items.deserialize_json(
                data["successful"]
            )
        )
    if "failed" in data:
        import aws_sdk_wickr.types.batch_device_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_device_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out
