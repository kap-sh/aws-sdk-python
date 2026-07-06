"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkListDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_id
    import aws_sdk_iot_wireless.types.device_certificate_list
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.sidewalk_id
    import aws_sdk_iot_wireless.types.sidewalk_manufacturing_sn
    import aws_sdk_iot_wireless.types.sidewalk_positioning
    import aws_sdk_iot_wireless.types.wireless_device_sidewalk_status


class SidewalkListDevice(TypedDict, closed=True):
    amazon_id: NotRequired["aws_sdk_iot_wireless.types.amazon_id.AmazonId"]
    """<p>The Sidewalk Amazon ID.</p>"""
    sidewalk_id: NotRequired["aws_sdk_iot_wireless.types.sidewalk_id.SidewalkId"]
    """<p>The sidewalk device identification.</p>"""
    sidewalk_manufacturing_sn: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_manufacturing_sn.SidewalkManufacturingSn"
    ]
    """<p>The Sidewalk manufacturing series number.</p>"""
    device_certificates: NotRequired[
        "aws_sdk_iot_wireless.types.device_certificate_list.DeviceCertificateList"
    ]
    """<p>The sidewalk device certificates for Ed25519 and P256r1.</p>"""
    device_profile_id: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>Sidewalk object used by list functions.</p>"""
    status: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_sidewalk_status.WirelessDeviceSidewalkStatus"
    ]
    """<p>The status of the Sidewalk devices, such as provisioned or registered.</p>"""
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkListDevice) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "sidewalk_id" in value:
        out["SidewalkId"] = value["sidewalk_id"]
    if "sidewalk_manufacturing_sn" in value:
        out["SidewalkManufacturingSn"] = value["sidewalk_manufacturing_sn"]
    if "device_certificates" in value:
        import aws_sdk_iot_wireless.types.device_certificate_list

        out["DeviceCertificates"] = (
            aws_sdk_iot_wireless.types.device_certificate_list.serialize_json(
                value["device_certificates"]
            )
        )
    if "device_profile_id" in value:
        out["DeviceProfileId"] = value["device_profile_id"]
    if "status" in value:
        import aws_sdk_iot_wireless.types.wireless_device_sidewalk_status

        out["Status"] = (
            aws_sdk_iot_wireless.types.wireless_device_sidewalk_status.serialize_json(
                value["status"]
            )
        )
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkListDevice:
    out: SidewalkListDevice = {}  # type: ignore[typeddict-item]
    if "AmazonId" in data:
        out["amazon_id"] = data["AmazonId"]
    if "SidewalkId" in data:
        out["sidewalk_id"] = data["SidewalkId"]
    if "SidewalkManufacturingSn" in data:
        out["sidewalk_manufacturing_sn"] = data["SidewalkManufacturingSn"]
    if "DeviceCertificates" in data:
        import aws_sdk_iot_wireless.types.device_certificate_list

        out["device_certificates"] = (
            aws_sdk_iot_wireless.types.device_certificate_list.deserialize_json(
                data["DeviceCertificates"]
            )
        )
    if "DeviceProfileId" in data:
        out["device_profile_id"] = data["DeviceProfileId"]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.wireless_device_sidewalk_status

        out["status"] = (
            aws_sdk_iot_wireless.types.wireless_device_sidewalk_status.deserialize_json(
                data["Status"]
            )
        )
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            aws_sdk_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
