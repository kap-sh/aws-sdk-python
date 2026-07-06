"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_delete_device_position_history_error_list


class BatchDeleteDevicePositionHistoryResponse(TypedDict, closed=True):
    errors: "aws_sdk_location.types.batch_delete_device_position_history_error_list.BatchDeleteDevicePositionHistoryErrorList"
    """<p>Contains error details for each device history that failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.batch_delete_device_position_history_error_list

    out["Errors"] = (
        aws_sdk_location.types.batch_delete_device_position_history_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDevicePositionHistoryResponse:
    out: BatchDeleteDevicePositionHistoryResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_location.types.batch_delete_device_position_history_error_list

        out["errors"] = (
            aws_sdk_location.types.batch_delete_device_position_history_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDevicePositionHistoryResponse.errors required"
        )
    return out
