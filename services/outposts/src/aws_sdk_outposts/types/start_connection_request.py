"""Generated from Smithy shape ``com.amazonaws.outposts#StartConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id
    import aws_sdk_outposts.types.device_serial_number
    import aws_sdk_outposts.types.network_interface_device_index
    import aws_sdk_outposts.types.wire_guard_public_key


class StartConnectionRequest(TypedDict):
    device_serial_number: NotRequired[
        "aws_sdk_outposts.types.device_serial_number.DeviceSerialNumber"
    ]
    """<p> The serial number of the dongle. </p>"""
    asset_id: "aws_sdk_outposts.types.asset_id.AssetId"
    """<p> The ID of the Outpost server.</p>"""
    client_public_key: "aws_sdk_outposts.types.wire_guard_public_key.WireGuardPublicKey"
    """<p> The public key of the client. </p>"""
    network_interface_device_index: "aws_sdk_outposts.types.network_interface_device_index.NetworkInterfaceDeviceIndex"
    """<p> The device index of the network interface on the Outpost server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConnectionRequest) -> dict:
    out: dict = {}
    if "device_serial_number" in value:
        out["DeviceSerialNumber"] = value["device_serial_number"]
    out["AssetId"] = value["asset_id"]
    out["ClientPublicKey"] = value["client_public_key"]
    out["NetworkInterfaceDeviceIndex"] = value.get("network_interface_device_index", 0)
    return out


def deserialize_json(data: dict) -> StartConnectionRequest:
    out: StartConnectionRequest = {}  # type: ignore[typeddict-item]
    if "DeviceSerialNumber" in data:
        out["device_serial_number"] = data["DeviceSerialNumber"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    else:
        raise DeserializationError("StartConnectionRequest.asset_id required")
    if "ClientPublicKey" in data:
        out["client_public_key"] = data["ClientPublicKey"]
    else:
        raise DeserializationError("StartConnectionRequest.client_public_key required")
    if "NetworkInterfaceDeviceIndex" in data:
        out["network_interface_device_index"] = data["NetworkInterfaceDeviceIndex"]
    else:
        out["network_interface_device_index"] = 0
    return out
