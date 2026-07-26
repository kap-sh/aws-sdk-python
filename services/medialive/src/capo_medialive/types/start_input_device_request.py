"""Generated from Smithy shape ``com.amazonaws.medialive#StartInputDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class StartInputDeviceRequest(TypedDict, closed=True):
    input_device_id: "capo_medialive.types.__string.__string"
    """The unique ID of the input device to start. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: StartInputDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartInputDeviceRequest:
    out: StartInputDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
