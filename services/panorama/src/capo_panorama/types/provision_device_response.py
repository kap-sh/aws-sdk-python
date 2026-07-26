"""Generated from Smithy shape ``com.amazonaws.panorama#ProvisionDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.certificates
    import capo_panorama.types.device_arn
    import capo_panorama.types.device_id
    import capo_panorama.types.device_status
    import capo_panorama.types.iot_thing_name


class ProvisionDeviceResponse(TypedDict, closed=True):
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""
    arn: "capo_panorama.types.device_arn.DeviceArn"
    """<p>The device's ARN.</p>"""
    status: "capo_panorama.types.device_status.DeviceStatus"
    """<p>The device's status.</p>"""
    certificates: NotRequired["capo_panorama.types.certificates.Certificates"]
    """<p>The device's configuration bundle.</p>"""
    iot_thing_name: NotRequired["capo_panorama.types.iot_thing_name.IotThingName"]
    """<p>The device's IoT thing name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionDeviceResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    out["Arn"] = value["arn"]
    out["Status"] = value["status"]
    if "certificates" in value:
        import capo_panorama.types.certificates

        out["Certificates"] = capo_panorama.types.certificates.serialize_json(
            value["certificates"]
        )
    if "iot_thing_name" in value:
        out["IotThingName"] = value["iot_thing_name"]
    return out


def deserialize_json(data: dict) -> ProvisionDeviceResponse:
    out: ProvisionDeviceResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ProvisionDeviceResponse.arn required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("ProvisionDeviceResponse.status required")
    if "Certificates" in data:
        import capo_panorama.types.certificates

        out["certificates"] = capo_panorama.types.certificates.deserialize_json(
            data["Certificates"]
        )
    if "IotThingName" in data:
        out["iot_thing_name"] = data["IotThingName"]
    return out
