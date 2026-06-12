"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANUpdateDevice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.service_profile_id
    import aws_sdk_iot_wireless.types.update_abp_v1_0_x
    import aws_sdk_iot_wireless.types.update_abp_v1_1
    import aws_sdk_iot_wireless.types.update_f_ports


class LoRaWANUpdateDevice(TypedDict):
    device_profile_id: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>The ID of the device profile for the wireless device.</p>"""
    service_profile_id: NotRequired[
        "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"
    ]
    """<p>The ID of the service profile.</p>"""
    abp_v1_1: NotRequired["aws_sdk_iot_wireless.types.update_abp_v1_1.UpdateAbpV1_1"]
    """<p>ABP device object for update APIs for v1.1</p>"""
    abp_v1_0_x: NotRequired[
        "aws_sdk_iot_wireless.types.update_abp_v1_0_x.UpdateAbpV1_0_x"
    ]
    """<p>ABP device object for update APIs for v1.0.x</p>"""
    f_ports: NotRequired["aws_sdk_iot_wireless.types.update_f_ports.UpdateFPorts"]
    """<p>FPorts object for the positioning information of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANUpdateDevice) -> dict:
    out: dict = {}
    if "device_profile_id" in value:
        out["DeviceProfileId"] = value["device_profile_id"]
    if "service_profile_id" in value:
        out["ServiceProfileId"] = value["service_profile_id"]
    if "abp_v1_1" in value:
        import aws_sdk_iot_wireless.types.update_abp_v1_1

        out["AbpV1_1"] = aws_sdk_iot_wireless.types.update_abp_v1_1.serialize_json(
            value["abp_v1_1"]
        )
    if "abp_v1_0_x" in value:
        import aws_sdk_iot_wireless.types.update_abp_v1_0_x

        out["AbpV1_0_x"] = aws_sdk_iot_wireless.types.update_abp_v1_0_x.serialize_json(
            value["abp_v1_0_x"]
        )
    if "f_ports" in value:
        import aws_sdk_iot_wireless.types.update_f_ports

        out["FPorts"] = aws_sdk_iot_wireless.types.update_f_ports.serialize_json(
            value["f_ports"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANUpdateDevice:
    out: LoRaWANUpdateDevice = {}  # type: ignore[typeddict-item]
    if "DeviceProfileId" in data:
        out["device_profile_id"] = data["DeviceProfileId"]
    if "ServiceProfileId" in data:
        out["service_profile_id"] = data["ServiceProfileId"]
    if "AbpV1_1" in data:
        import aws_sdk_iot_wireless.types.update_abp_v1_1

        out["abp_v1_1"] = aws_sdk_iot_wireless.types.update_abp_v1_1.deserialize_json(
            data["AbpV1_1"]
        )
    if "AbpV1_0_x" in data:
        import aws_sdk_iot_wireless.types.update_abp_v1_0_x

        out["abp_v1_0_x"] = (
            aws_sdk_iot_wireless.types.update_abp_v1_0_x.deserialize_json(
                data["AbpV1_0_x"]
            )
        )
    if "FPorts" in data:
        import aws_sdk_iot_wireless.types.update_f_ports

        out["f_ports"] = aws_sdk_iot_wireless.types.update_f_ports.deserialize_json(
            data["FPorts"]
        )
    return out
