"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StartDeviceDiscoveryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_discovery_id
    import aws_sdk_iot_managed_integrations.types.discovery_started_at


class StartDeviceDiscoveryResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    ]
    """<p>The id of the device discovery job request.</p>"""
    started_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.discovery_started_at.DiscoveryStartedAt"
    ]
    """<p>The timestamp value for the start time of the device discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeviceDiscoveryResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "started_at" in value:
        import aws_sdk_iot_managed_integrations.types.discovery_started_at

        out["StartedAt"] = (
            aws_sdk_iot_managed_integrations.types.discovery_started_at.serialize_json(
                value["started_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartDeviceDiscoveryResponse:
    out: StartDeviceDiscoveryResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "StartedAt" in data:
        import aws_sdk_iot_managed_integrations.types.discovery_started_at

        out["started_at"] = (
            aws_sdk_iot_managed_integrations.types.discovery_started_at.deserialize_json(
                data["StartedAt"]
            )
        )
    return out
