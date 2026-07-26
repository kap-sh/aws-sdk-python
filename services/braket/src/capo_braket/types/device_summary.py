"""Generated from Smithy shape ``com.amazonaws.braket#DeviceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import capo_braket.types.device_arn
    import capo_braket.types.device_status
    import capo_braket.types.device_type


class DeviceSummary(TypedDict, closed=True):
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device.</p>"""
    device_name: "str"
    """<p>The name of the device.</p>"""
    provider_name: "str"
    """<p>The provider of the device.</p>"""
    device_type: "capo_braket.types.device_type.DeviceType"
    """<p>The type of the device.</p>"""
    device_status: "capo_braket.types.device_status.DeviceStatus"
    """<p>The status of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummary) -> dict:
    out: dict = {}
    out["deviceArn"] = value["device_arn"]
    out["deviceName"] = value["device_name"]
    out["providerName"] = value["provider_name"]
    out["deviceType"] = value["device_type"]
    out["deviceStatus"] = value["device_status"]
    return out


def deserialize_json(data: dict) -> DeviceSummary:
    out: DeviceSummary = {}  # type: ignore[typeddict-item]
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("DeviceSummary.device_arn required")
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    else:
        raise DeserializationError("DeviceSummary.device_name required")
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    else:
        raise DeserializationError("DeviceSummary.provider_name required")
    if "deviceType" in data:
        out["device_type"] = data["deviceType"]
    else:
        raise DeserializationError("DeviceSummary.device_type required")
    if "deviceStatus" in data:
        out["device_status"] = data["deviceStatus"]
    else:
        raise DeserializationError("DeviceSummary.device_status required")
    return out
