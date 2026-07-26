"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeviceDiscoverySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.device_discovery_status
    import capo_iot_managed_integrations.types.discovery_type


class DeviceDiscoverySummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    ]
    """<p>The unique identifier of the device discovery job.</p>"""
    discovery_type: NotRequired[
        "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
    ]
    """<p>The type of discovery process used to find devices.</p>"""
    status: NotRequired[
        "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
    ]
    """<p>The current status of the device discovery job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDiscoverySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "discovery_type" in value:
        import capo_iot_managed_integrations.types.discovery_type

        out["DiscoveryType"] = (
            capo_iot_managed_integrations.types.discovery_type.serialize_json(
                value["discovery_type"]
            )
        )
    if "status" in value:
        import capo_iot_managed_integrations.types.device_discovery_status

        out["Status"] = (
            capo_iot_managed_integrations.types.device_discovery_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeviceDiscoverySummary:
    out: DeviceDiscoverySummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DiscoveryType" in data:
        import capo_iot_managed_integrations.types.discovery_type

        out["discovery_type"] = (
            capo_iot_managed_integrations.types.discovery_type.deserialize_json(
                data["DiscoveryType"]
            )
        )
    if "Status" in data:
        import capo_iot_managed_integrations.types.device_discovery_status

        out["status"] = (
            capo_iot_managed_integrations.types.device_discovery_status.deserialize_json(
                data["Status"]
            )
        )
    return out
