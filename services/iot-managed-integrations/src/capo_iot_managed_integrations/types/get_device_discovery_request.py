"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDeviceDiscoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.device_discovery_id


class GetDeviceDiscoveryRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    )
    """<p>The id of the device discovery job request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceDiscoveryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeviceDiscoveryRequest:
    out: GetDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    return out
