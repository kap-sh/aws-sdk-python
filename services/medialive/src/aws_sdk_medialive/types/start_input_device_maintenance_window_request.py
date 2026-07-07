"""Generated from Smithy shape ``com.amazonaws.medialive#StartInputDeviceMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StartInputDeviceMaintenanceWindowRequest(TypedDict, closed=True):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of the input device to start a maintenance window for. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: StartInputDeviceMaintenanceWindowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartInputDeviceMaintenanceWindowRequest:
    out: StartInputDeviceMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    return out
