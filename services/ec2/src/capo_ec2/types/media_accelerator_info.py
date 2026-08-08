"""Generated from Smithy shape ``com.amazonaws.ec2#MediaAcceleratorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.media_device_info_list
    import capo_ec2.types.total_media_memory


class MediaAcceleratorInfo(TypedDict, closed=True):
    accelerators: NotRequired[
        "capo_ec2.types.media_device_info_list.MediaDeviceInfoList"
    ]
    """<p>Describes the media accelerators for the instance type.</p>"""
    total_media_memory_in_mi_b: NotRequired[
        "capo_ec2.types.total_media_memory.TotalMediaMemory"
    ]
    """<p>The total size of the memory for the media accelerators for the instance type, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MediaAcceleratorInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "accelerators" in value:
        import capo_ec2.types.media_device_info_list

        capo_ec2.types.media_device_info_list.serialize_ec2_query(
            value["accelerators"], pairs, f"{key_prefix}Accelerators"
        )
    if "total_media_memory_in_mi_b" in value:
        pairs.append(
            (
                f"{key_prefix}TotalMediaMemoryInMiB",
                str(value["total_media_memory_in_mi_b"]),
            )
        )


def deserialize_ec2_query(el: Element) -> MediaAcceleratorInfo:
    out: MediaAcceleratorInfo = {}  # type: ignore[typeddict-item]
    if el.find("accelerators") is not None:
        import capo_ec2.types.media_device_info_list

        out["accelerators"] = (
            capo_ec2.types.media_device_info_list.deserialize_ec2_query(
                el, "accelerators"
            )
        )
    child_total_media_memory_in_mi_b = el.find("totalMediaMemoryInMiB")
    if child_total_media_memory_in_mi_b is not None:
        out["total_media_memory_in_mi_b"] = int(
            child_total_media_memory_in_mi_b.text or ""
        )
    return out
