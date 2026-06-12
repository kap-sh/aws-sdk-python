"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDeviceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_discovery_id


class GetDeviceDiscoveryRequest(TypedDict):
    identifier: (
        "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    )
    """<p>The id of the device discovery job request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceDiscoveryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeviceDiscoveryRequest:
    out: GetDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    return out
