"""Generated from Smithy shape ``com.amazonaws.ec2#MediaDeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.media_device_count
    import capo_ec2.types.media_device_manufacturer_name
    import capo_ec2.types.media_device_memory_info
    import capo_ec2.types.media_device_name


class MediaDeviceInfo(TypedDict, closed=True):
    count: NotRequired["capo_ec2.types.media_device_count.MediaDeviceCount"]
    """<p>The number of media accelerators for the instance type.</p>"""
    name: NotRequired["capo_ec2.types.media_device_name.MediaDeviceName"]
    """<p>The name of the media accelerator.</p>"""
    manufacturer: NotRequired[
        "capo_ec2.types.media_device_manufacturer_name.MediaDeviceManufacturerName"
    ]
    """<p>The manufacturer of the media accelerator.</p>"""
    memory_info: NotRequired[
        "capo_ec2.types.media_device_memory_info.MediaDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the media accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MediaDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "count" in value:
        pairs.append((f"{key_prefix}Count", str(value["count"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "manufacturer" in value:
        pairs.append((f"{key_prefix}Manufacturer", str(value["manufacturer"])))
    if "memory_info" in value:
        import capo_ec2.types.media_device_memory_info

        capo_ec2.types.media_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{key_prefix}MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> MediaDeviceInfo:
    out: MediaDeviceInfo = {}  # type: ignore[typeddict-item]
    child_count = el.find("count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_manufacturer = el.find("manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    child_memory_info = el.find("memoryInfo")
    if child_memory_info is not None:
        import capo_ec2.types.media_device_memory_info

        out["memory_info"] = (
            capo_ec2.types.media_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
