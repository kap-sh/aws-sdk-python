"""Generated from Smithy shape ``com.amazonaws.medialive#AcceptInputDeviceTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class AcceptInputDeviceTransferRequest(TypedDict, closed=True):
    input_device_id: "capo_medialive.types.__string.__string"
    """The unique ID of the input device to accept. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInputDeviceTransferRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptInputDeviceTransferRequest:
    out: AcceptInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
    return out
