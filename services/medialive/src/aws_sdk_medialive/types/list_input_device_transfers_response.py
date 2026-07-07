"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputDeviceTransfersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_transferring_input_device_summary
    import aws_sdk_medialive.types.__string


class ListInputDeviceTransfersResponse(TypedDict, closed=True):
    input_device_transfers: NotRequired[
        "aws_sdk_medialive.types.__list_of_transferring_input_device_summary.__listOfTransferringInputDeviceSummary"
    ]
    """The list of devices that you are transferring or are being transferred to you."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A token to get additional list results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputDeviceTransfersResponse) -> dict:
    out: dict = {}
    if "input_device_transfers" in value:
        import aws_sdk_medialive.types.__list_of_transferring_input_device_summary

        out["inputDeviceTransfers"] = (
            aws_sdk_medialive.types.__list_of_transferring_input_device_summary.serialize_json(
                value["input_device_transfers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputDeviceTransfersResponse:
    out: ListInputDeviceTransfersResponse = {}  # type: ignore[typeddict-item]
    if "inputDeviceTransfers" in data:
        import aws_sdk_medialive.types.__list_of_transferring_input_device_summary

        out["input_device_transfers"] = (
            aws_sdk_medialive.types.__list_of_transferring_input_device_summary.deserialize_json(
                data["inputDeviceTransfers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
