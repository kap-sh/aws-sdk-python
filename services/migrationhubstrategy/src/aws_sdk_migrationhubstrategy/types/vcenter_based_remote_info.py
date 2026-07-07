"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#VcenterBasedRemoteInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.os_type
    import aws_sdk_migrationhubstrategy.types.string


class VcenterBasedRemoteInfo(TypedDict, closed=True):
    vcenter_configuration_time_stamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p>The time when the remote server based on vCenter was last configured.</p>"""
    os_type: NotRequired["aws_sdk_migrationhubstrategy.types.os_type.OSType"]
    """<p>The type of the operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VcenterBasedRemoteInfo) -> dict:
    out: dict = {}
    if "vcenter_configuration_time_stamp" in value:
        out["vcenterConfigurationTimeStamp"] = value["vcenter_configuration_time_stamp"]
    if "os_type" in value:
        out["osType"] = value["os_type"]
    return out


def deserialize_json(data: dict) -> VcenterBasedRemoteInfo:
    out: VcenterBasedRemoteInfo = {}  # type: ignore[typeddict-item]
    if "vcenterConfigurationTimeStamp" in data:
        out["vcenter_configuration_time_stamp"] = data["vcenterConfigurationTimeStamp"]
    if "osType" in data:
        out["os_type"] = data["osType"]
    return out
