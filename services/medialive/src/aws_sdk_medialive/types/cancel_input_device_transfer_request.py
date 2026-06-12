"""Generated from Smithy shape ``com.amazonaws.medialive#CancelInputDeviceTransferRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class CancelInputDeviceTransferRequest(TypedDict):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of the input device to cancel. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: CancelInputDeviceTransferRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelInputDeviceTransferRequest:
    out: CancelInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
    return out
