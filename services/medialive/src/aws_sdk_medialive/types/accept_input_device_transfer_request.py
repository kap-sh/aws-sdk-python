"""Generated from Smithy shape ``com.amazonaws.medialive#AcceptInputDeviceTransferRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class AcceptInputDeviceTransferRequest(TypedDict):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of the input device to accept. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInputDeviceTransferRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptInputDeviceTransferRequest:
    out: AcceptInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
    return out
