"""Generated from Smithy shape ``com.amazonaws.connect#DeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.operating_system
    import capo_connect.types.platform_name
    import capo_connect.types.platform_version


class DeviceInfo(TypedDict, closed=True):
    platform_name: NotRequired["capo_connect.types.platform_name.PlatformName"]
    """<p>Name of the platform that the participant used for the call.</p>"""
    platform_version: NotRequired["capo_connect.types.platform_version.PlatformVersion"]
    """<p>Version of the platform that the participant used for the call.</p>"""
    operating_system: NotRequired["capo_connect.types.operating_system.OperatingSystem"]
    """<p>Operating system that the participant used for the call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceInfo) -> dict:
    out: dict = {}
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "operating_system" in value:
        out["OperatingSystem"] = value["operating_system"]
    return out


def deserialize_json(data: dict) -> DeviceInfo:
    out: DeviceInfo = {}  # type: ignore[typeddict-item]
    if "PlatformName" in data:
        out["platform_name"] = data["PlatformName"]
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "OperatingSystem" in data:
        out["operating_system"] = data["OperatingSystem"]
    return out
