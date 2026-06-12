"""Generated from Smithy shape ``com.amazonaws.medialive#StopInputDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StopInputDeviceRequest(TypedDict):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of the input device to stop. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: StopInputDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopInputDeviceRequest:
    out: StopInputDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
