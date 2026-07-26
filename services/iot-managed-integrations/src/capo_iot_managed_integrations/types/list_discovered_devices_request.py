"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDiscoveredDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token


class ListDiscoveredDevicesRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    )
    """<p>The identifier of the device discovery job to list discovered devices for.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of discovered devices to return in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoveredDevicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDiscoveredDevicesRequest:
    out: ListDiscoveredDevicesRequest = {}  # type: ignore[typeddict-item]
    return out
