"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceMinutes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.double


class DeviceMinutes(TypedDict):
    total: NotRequired["aws_sdk_device_farm.types.double.Double"]
    """<p>When specified, represents the total minutes used by the resource to run tests.</p>"""
    metered: NotRequired["aws_sdk_device_farm.types.double.Double"]
    """<p>When specified, represents only the sum of metered minutes used by the resource to run tests.</p>"""
    unmetered: NotRequired["aws_sdk_device_farm.types.double.Double"]
    """<p>When specified, represents only the sum of unmetered minutes used by the resource to run tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceMinutes) -> dict:
    out: dict = {}
    if "total" in value:
        out["total"] = value["total"]
    if "metered" in value:
        out["metered"] = value["metered"]
    if "unmetered" in value:
        out["unmetered"] = value["unmetered"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceMinutes:
    out: DeviceMinutes = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    if "metered" in data:
        out["metered"] = data["metered"]
    if "unmetered" in data:
        out["unmetered"] = data["unmetered"]
    return out
