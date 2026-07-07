"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.abp_v1_0_x
    import aws_sdk_iot_wireless.types.abp_v1_1
    import aws_sdk_iot_wireless.types.dev_eui
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.f_ports
    import aws_sdk_iot_wireless.types.otaa_v1_0_x
    import aws_sdk_iot_wireless.types.otaa_v1_1
    import aws_sdk_iot_wireless.types.service_profile_id


class LoRaWANDevice(TypedDict, closed=True):
    dev_eui: NotRequired["aws_sdk_iot_wireless.types.dev_eui.DevEui"]
    """<p>The DevEUI value.</p>"""
    device_profile_id: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>The ID of the device profile for the new wireless device.</p>"""
    service_profile_id: NotRequired[
        "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"
    ]
    """<p>The ID of the service profile.</p>"""
    otaa_v1_1: NotRequired["aws_sdk_iot_wireless.types.otaa_v1_1.OtaaV1_1"]
    """<p>OTAA device object for v1.1 for create APIs</p>"""
    otaa_v1_0_x: NotRequired["aws_sdk_iot_wireless.types.otaa_v1_0_x.OtaaV1_0_x"]
    """<p>OTAA device object for create APIs for v1.0.x</p>"""
    abp_v1_1: NotRequired["aws_sdk_iot_wireless.types.abp_v1_1.AbpV1_1"]
    """<p>ABP device object for create APIs for v1.1</p>"""
    abp_v1_0_x: NotRequired["aws_sdk_iot_wireless.types.abp_v1_0_x.AbpV1_0_x"]
    """<p>LoRaWAN object for create APIs</p>"""
    f_ports: NotRequired["aws_sdk_iot_wireless.types.f_ports.FPorts"]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANDevice) -> dict:
    out: dict = {}
    if "dev_eui" in value:
        out["DevEui"] = value["dev_eui"]
    if "device_profile_id" in value:
        out["DeviceProfileId"] = value["device_profile_id"]
    if "service_profile_id" in value:
        out["ServiceProfileId"] = value["service_profile_id"]
    if "otaa_v1_1" in value:
        import aws_sdk_iot_wireless.types.otaa_v1_1

        out["OtaaV1_1"] = aws_sdk_iot_wireless.types.otaa_v1_1.serialize_json(
            value["otaa_v1_1"]
        )
    if "otaa_v1_0_x" in value:
        import aws_sdk_iot_wireless.types.otaa_v1_0_x

        out["OtaaV1_0_x"] = aws_sdk_iot_wireless.types.otaa_v1_0_x.serialize_json(
            value["otaa_v1_0_x"]
        )
    if "abp_v1_1" in value:
        import aws_sdk_iot_wireless.types.abp_v1_1

        out["AbpV1_1"] = aws_sdk_iot_wireless.types.abp_v1_1.serialize_json(
            value["abp_v1_1"]
        )
    if "abp_v1_0_x" in value:
        import aws_sdk_iot_wireless.types.abp_v1_0_x

        out["AbpV1_0_x"] = aws_sdk_iot_wireless.types.abp_v1_0_x.serialize_json(
            value["abp_v1_0_x"]
        )
    if "f_ports" in value:
        import aws_sdk_iot_wireless.types.f_ports

        out["FPorts"] = aws_sdk_iot_wireless.types.f_ports.serialize_json(
            value["f_ports"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANDevice:
    out: LoRaWANDevice = {}  # type: ignore[typeddict-item]
    if "DevEui" in data:
        out["dev_eui"] = data["DevEui"]
    if "DeviceProfileId" in data:
        out["device_profile_id"] = data["DeviceProfileId"]
    if "ServiceProfileId" in data:
        out["service_profile_id"] = data["ServiceProfileId"]
    if "OtaaV1_1" in data:
        import aws_sdk_iot_wireless.types.otaa_v1_1

        out["otaa_v1_1"] = aws_sdk_iot_wireless.types.otaa_v1_1.deserialize_json(
            data["OtaaV1_1"]
        )
    if "OtaaV1_0_x" in data:
        import aws_sdk_iot_wireless.types.otaa_v1_0_x

        out["otaa_v1_0_x"] = aws_sdk_iot_wireless.types.otaa_v1_0_x.deserialize_json(
            data["OtaaV1_0_x"]
        )
    if "AbpV1_1" in data:
        import aws_sdk_iot_wireless.types.abp_v1_1

        out["abp_v1_1"] = aws_sdk_iot_wireless.types.abp_v1_1.deserialize_json(
            data["AbpV1_1"]
        )
    if "AbpV1_0_x" in data:
        import aws_sdk_iot_wireless.types.abp_v1_0_x

        out["abp_v1_0_x"] = aws_sdk_iot_wireless.types.abp_v1_0_x.deserialize_json(
            data["AbpV1_0_x"]
        )
    if "FPorts" in data:
        import aws_sdk_iot_wireless.types.f_ports

        out["f_ports"] = aws_sdk_iot_wireless.types.f_ports.deserialize_json(
            data["FPorts"]
        )
    return out
