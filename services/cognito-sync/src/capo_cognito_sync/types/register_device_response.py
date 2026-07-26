"""Generated from Smithy shape ``com.amazonaws.cognitosync#RegisterDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.device_id


class RegisterDeviceResponse(TypedDict, closed=True):
    device_id: NotRequired["capo_cognito_sync.types.device_id.DeviceId"]
    """<p>The unique ID generated for this device by Cognito.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterDeviceResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    return out


def deserialize_json(data: dict) -> RegisterDeviceResponse:
    out: RegisterDeviceResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    return out
