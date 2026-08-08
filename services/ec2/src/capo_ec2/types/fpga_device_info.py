"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaDeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fpga_device_count
    import capo_ec2.types.fpga_device_manufacturer_name
    import capo_ec2.types.fpga_device_memory_info
    import capo_ec2.types.fpga_device_name


class FpgaDeviceInfo(TypedDict, closed=True):
    name: NotRequired["capo_ec2.types.fpga_device_name.FpgaDeviceName"]
    """<p>The name of the FPGA accelerator.</p>"""
    manufacturer: NotRequired[
        "capo_ec2.types.fpga_device_manufacturer_name.FpgaDeviceManufacturerName"
    ]
    """<p>The manufacturer of the FPGA accelerator.</p>"""
    count: NotRequired["capo_ec2.types.fpga_device_count.FpgaDeviceCount"]
    """<p>The count of FPGA accelerators for the instance type.</p>"""
    memory_info: NotRequired[
        "capo_ec2.types.fpga_device_memory_info.FpgaDeviceMemoryInfo"
    ]
    """<p>Describes the memory for the FPGA accelerator for the instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "manufacturer" in value:
        pairs.append((f"{key_prefix}Manufacturer", str(value["manufacturer"])))
    if "count" in value:
        pairs.append((f"{key_prefix}Count", str(value["count"])))
    if "memory_info" in value:
        import capo_ec2.types.fpga_device_memory_info

        capo_ec2.types.fpga_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{key_prefix}MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> FpgaDeviceInfo:
    out: FpgaDeviceInfo = {}  # type: ignore[typeddict-item]
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_manufacturer = el.find("manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    child_count = el.find("count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_memory_info = el.find("memoryInfo")
    if child_memory_info is not None:
        import capo_ec2.types.fpga_device_memory_info

        out["memory_info"] = (
            capo_ec2.types.fpga_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
