"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_id
    import capo_iot_wireless.types.dak_certificate_id
    import capo_iot_wireless.types.device_certificate_list
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.private_keys_list
    import capo_iot_wireless.types.sidewalk_id
    import capo_iot_wireless.types.sidewalk_manufacturing_sn
    import capo_iot_wireless.types.sidewalk_positioning
    import capo_iot_wireless.types.wireless_device_sidewalk_status


class SidewalkDevice(TypedDict, closed=True):
    amazon_id: NotRequired["capo_iot_wireless.types.amazon_id.AmazonId"]
    sidewalk_id: NotRequired["capo_iot_wireless.types.sidewalk_id.SidewalkId"]
    """<p>The sidewalk device identification.</p>"""
    sidewalk_manufacturing_sn: NotRequired[
        "capo_iot_wireless.types.sidewalk_manufacturing_sn.SidewalkManufacturingSn"
    ]
    """<p>The Sidewalk manufacturing series number.</p>"""
    device_certificates: NotRequired[
        "capo_iot_wireless.types.device_certificate_list.DeviceCertificateList"
    ]
    """<p>The sidewalk device certificates for Ed25519 and P256r1.</p>"""
    private_keys: NotRequired[
        "capo_iot_wireless.types.private_keys_list.PrivateKeysList"
    ]
    """<p>The Sidewalk device private keys that will be used for onboarding the device.</p>"""
    device_profile_id: NotRequired[
        "capo_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>The ID of the Sidewalk device profile.</p>"""
    certificate_id: NotRequired[
        "capo_iot_wireless.types.dak_certificate_id.DakCertificateId"
    ]
    """<p>The ID of the Sidewalk device profile.</p>"""
    status: NotRequired[
        "capo_iot_wireless.types.wireless_device_sidewalk_status.WirelessDeviceSidewalkStatus"
    ]
    """<p>The Sidewalk device status, such as provisioned or registered.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkDevice) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "sidewalk_id" in value:
        out["SidewalkId"] = value["sidewalk_id"]
    if "sidewalk_manufacturing_sn" in value:
        out["SidewalkManufacturingSn"] = value["sidewalk_manufacturing_sn"]
    if "device_certificates" in value:
        import capo_iot_wireless.types.device_certificate_list

        out["DeviceCertificates"] = (
            capo_iot_wireless.types.device_certificate_list.serialize_json(
                value["device_certificates"]
            )
        )
    if "private_keys" in value:
        import capo_iot_wireless.types.private_keys_list

        out["PrivateKeys"] = capo_iot_wireless.types.private_keys_list.serialize_json(
            value["private_keys"]
        )
    if "device_profile_id" in value:
        out["DeviceProfileId"] = value["device_profile_id"]
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "status" in value:
        import capo_iot_wireless.types.wireless_device_sidewalk_status

        out["Status"] = (
            capo_iot_wireless.types.wireless_device_sidewalk_status.serialize_json(
                value["status"]
            )
        )
    if "positioning" in value:
        import capo_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkDevice:
    out: SidewalkDevice = {}  # type: ignore[typeddict-item]
    if "AmazonId" in data:
        out["amazon_id"] = data["AmazonId"]
    if "SidewalkId" in data:
        out["sidewalk_id"] = data["SidewalkId"]
    if "SidewalkManufacturingSn" in data:
        out["sidewalk_manufacturing_sn"] = data["SidewalkManufacturingSn"]
    if "DeviceCertificates" in data:
        import capo_iot_wireless.types.device_certificate_list

        out["device_certificates"] = (
            capo_iot_wireless.types.device_certificate_list.deserialize_json(
                data["DeviceCertificates"]
            )
        )
    if "PrivateKeys" in data:
        import capo_iot_wireless.types.private_keys_list

        out["private_keys"] = (
            capo_iot_wireless.types.private_keys_list.deserialize_json(
                data["PrivateKeys"]
            )
        )
    if "DeviceProfileId" in data:
        out["device_profile_id"] = data["DeviceProfileId"]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    if "Status" in data:
        import capo_iot_wireless.types.wireless_device_sidewalk_status

        out["status"] = (
            capo_iot_wireless.types.wireless_device_sidewalk_status.deserialize_json(
                data["Status"]
            )
        )
    if "Positioning" in data:
        import capo_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
