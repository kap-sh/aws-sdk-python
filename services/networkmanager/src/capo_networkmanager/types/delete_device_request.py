"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id


class DeleteDeviceRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeviceRequest:
    out: DeleteDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
