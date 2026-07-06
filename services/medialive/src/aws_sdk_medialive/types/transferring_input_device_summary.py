"""Generated from Smithy shape ``com.amazonaws.medialive#TransferringInputDeviceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_device_transfer_type


class TransferringInputDeviceSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID of the input device."""
    message: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The optional message that the sender has attached to the transfer."""
    target_customer_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The AWS account ID for the recipient of the input device transfer."""
    transfer_type: NotRequired[
        "aws_sdk_medialive.types.input_device_transfer_type.InputDeviceTransferType"
    ]
    """The type (direction) of the input device transfer."""


# --- restJson1 ser/de ---
def serialize_json(value: TransferringInputDeviceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    if "target_customer_id" in value:
        out["targetCustomerId"] = value["target_customer_id"]
    if "transfer_type" in value:
        import aws_sdk_medialive.types.input_device_transfer_type

        out["transferType"] = (
            aws_sdk_medialive.types.input_device_transfer_type.serialize_json(
                value["transfer_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransferringInputDeviceSummary:
    out: TransferringInputDeviceSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "message" in data:
        out["message"] = data["message"]
    if "targetCustomerId" in data:
        out["target_customer_id"] = data["targetCustomerId"]
    if "transferType" in data:
        import aws_sdk_medialive.types.input_device_transfer_type

        out["transfer_type"] = (
            aws_sdk_medialive.types.input_device_transfer_type.deserialize_json(
                data["transferType"]
            )
        )
    return out
