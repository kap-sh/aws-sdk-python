"""Generated from Smithy shape ``com.amazonaws.medialive#TransferInputDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class TransferInputDeviceRequest(TypedDict):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of this input device. For example, hd-123456789abcdef."""
    target_customer_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The AWS account ID (12 digits) for the recipient of the device transfer."""
    target_region: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The target AWS region to transfer the device."""
    transfer_message: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An optional message for the recipient. Maximum 280 characters."""


# --- restJson1 ser/de ---
def serialize_json(value: TransferInputDeviceRequest) -> dict:
    out: dict = {}
    if "target_customer_id" in value:
        out["targetCustomerId"] = value["target_customer_id"]
    if "target_region" in value:
        out["targetRegion"] = value["target_region"]
    if "transfer_message" in value:
        out["transferMessage"] = value["transfer_message"]
    return out


def deserialize_json(data: dict) -> TransferInputDeviceRequest:
    out: TransferInputDeviceRequest = {}  # type: ignore[typeddict-item]
    if "targetCustomerId" in data:
        out["target_customer_id"] = data["targetCustomerId"]
    if "targetRegion" in data:
        out["target_region"] = data["targetRegion"]
    if "transferMessage" in data:
        out["transfer_message"] = data["transferMessage"]
    return out
