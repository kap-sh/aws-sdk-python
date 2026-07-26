"""Generated from Smithy shape ``com.amazonaws.sagemaker#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_description
    import capo_sagemaker.types.device_name
    import capo_sagemaker.types.thing_name


class Device(TypedDict, closed=True):
    device_name: NotRequired["capo_sagemaker.types.device_name.DeviceName"]
    """<p>The name of the device.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.device_description.DeviceDescription"
    ]
    """<p>Description of the device.</p>"""
    iot_thing_name: NotRequired["capo_sagemaker.types.thing_name.ThingName"]
    """<p>Amazon Web Services Internet of Things (IoT) object name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Device) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "iot_thing_name" in value:
        out["IotThingName"] = value["iot_thing_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "IotThingName" in data:
        out["iot_thing_name"] = data["IotThingName"]
    return out
