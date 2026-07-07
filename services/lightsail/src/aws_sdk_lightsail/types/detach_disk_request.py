"""Generated from Smithy shape ``com.amazonaws.lightsail#DetachDiskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DetachDiskRequest(TypedDict, closed=True):
    disk_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The unique name of the disk you want to detach from your instance (<code>my-disk</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachDiskRequest:
    out: DetachDiskRequest = {}  # type: ignore[typeddict-item]
    if "diskName" in data:
        out["disk_name"] = data["diskName"]
    else:
        raise DeserializationError("DetachDiskRequest.disk_name required")
    return out
