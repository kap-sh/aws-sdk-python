"""Generated from Smithy shape ``com.amazonaws.ec2#MediaDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.media_device_count
    import aws_sdk_ec2.types.media_device_manufacturer_name
    import aws_sdk_ec2.types.media_device_memory_info
    import aws_sdk_ec2.types.media_device_name


class MediaDeviceInfo(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.media_device_count.MediaDeviceCount"]
    """<p>The number of media accelerators for the instance type.</p>"""
    name: NotRequired["aws_sdk_ec2.types.media_device_name.MediaDeviceName"]
    """<p>The name of the media accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.media_device_manufacturer_name.MediaDeviceManufacturerName"
    ]
    """<p>The manufacturer of the media accelerator.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.media_device_memory_info.MediaDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the media accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MediaDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "manufacturer" in value:
        pairs.append((f"{prefix}.Manufacturer", str(value["manufacturer"])))
    if "memory_info" in value:
        import aws_sdk_ec2.types.media_device_memory_info

        aws_sdk_ec2.types.media_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{prefix}.MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> MediaDeviceInfo:
    out: MediaDeviceInfo = {}  # type: ignore[typeddict-item]
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_manufacturer = el.find("Manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    child_memory_info = el.find("MemoryInfo")
    if child_memory_info is not None:
        import aws_sdk_ec2.types.media_device_memory_info

        out["memory_info"] = (
            aws_sdk_ec2.types.media_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
