"""Generated from Smithy shape ``com.amazonaws.mgn#Disk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.positive_integer


class Disk(TypedDict, closed=True):
    device_name: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>The disk or device name.</p>"""
    bytes: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>The amount of storage on the disk in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Disk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    out["bytes"] = value.get("bytes", 0)
    return out


def deserialize_json(data: dict) -> Disk:
    out: Disk = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "bytes" in data:
        out["bytes"] = data["bytes"]
    else:
        out["bytes"] = 0
    return out
