"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#OSInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.os_type
    import aws_sdk_migrationhubstrategy.types.os_version


class OSInfo(TypedDict):
    type: NotRequired["aws_sdk_migrationhubstrategy.types.os_type.OSType"]
    """<p> Information about the type of operating system. </p>"""
    version: NotRequired["aws_sdk_migrationhubstrategy.types.os_version.OSVersion"]
    """<p> Information about the version of operating system. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OSInfo) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> OSInfo:
    out: OSInfo = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "version" in data:
        out["version"] = data["version"]
    return out
