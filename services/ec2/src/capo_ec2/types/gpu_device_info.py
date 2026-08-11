"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.gpu_device_count
    import capo_ec2.types.gpu_device_manufacturer_name
    import capo_ec2.types.gpu_device_memory_info
    import capo_ec2.types.gpu_device_name
    import capo_ec2.types.gpu_partition_size
    import capo_ec2.types.logical_gpu_count
    import capo_ec2.types.workloads_list


class GpuDeviceInfo(TypedDict, closed=True):
    name: NotRequired["capo_ec2.types.gpu_device_name.GpuDeviceName"]
    """<p>The name of the GPU accelerator.</p>"""
    manufacturer: NotRequired[
        "capo_ec2.types.gpu_device_manufacturer_name.GpuDeviceManufacturerName"
    ]
    """<p>The manufacturer of the GPU accelerator.</p>"""
    count: NotRequired["capo_ec2.types.gpu_device_count.GpuDeviceCount"]
    """<p>The number of GPUs for the instance type.</p>"""
    logical_gpu_count: NotRequired["capo_ec2.types.logical_gpu_count.LogicalGpuCount"]
    """<p>Total number of GPU devices of this type.</p>"""
    gpu_partition_size: NotRequired[
        "capo_ec2.types.gpu_partition_size.GpuPartitionSize"
    ]
    """<p>The size of each GPU as a fraction of a full GPU, between 0 (excluded) and 1 (included).</p>"""
    workloads: NotRequired["capo_ec2.types.workloads_list.WorkloadsList"]
    """<p>A list of workload types this GPU supports.</p>"""
    memory_info: NotRequired[
        "capo_ec2.types.gpu_device_memory_info.GpuDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the GPU accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GpuDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "manufacturer" in value:
        pairs.append((f"{key_prefix}Manufacturer", str(value["manufacturer"])))
    if "count" in value:
        pairs.append((f"{key_prefix}Count", str(value["count"])))
    if "logical_gpu_count" in value:
        pairs.append((f"{key_prefix}LogicalGpuCount", str(value["logical_gpu_count"])))
    if "gpu_partition_size" in value:
        pairs.append(
            (
                f"{key_prefix}GpuPartitionSize",
                (
                    "NaN"
                    if value["gpu_partition_size"] != value["gpu_partition_size"]
                    else "Infinity"
                    if value["gpu_partition_size"] == float("inf")
                    else "-Infinity"
                    if value["gpu_partition_size"] == float("-inf")
                    else str(value["gpu_partition_size"])
                ),
            )
        )
    if "workloads" in value:
        import capo_ec2.types.workloads_list

        capo_ec2.types.workloads_list.serialize_ec2_query(
            value["workloads"], pairs, f"{key_prefix}WorkloadSet"
        )
    if "memory_info" in value:
        import capo_ec2.types.gpu_device_memory_info

        capo_ec2.types.gpu_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{key_prefix}MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> GpuDeviceInfo:
    out: GpuDeviceInfo = {}  # type: ignore[typeddict-item]
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_manufacturer = el.find("manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    child_count = el.find("count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_logical_gpu_count = el.find("logicalGpuCount")
    if child_logical_gpu_count is not None:
        out["logical_gpu_count"] = int(child_logical_gpu_count.text or "")
    child_gpu_partition_size = el.find("gpuPartitionSize")
    if child_gpu_partition_size is not None:
        out["gpu_partition_size"] = float(child_gpu_partition_size.text or "")
    child_workloads = el.find("workloadSet")
    if child_workloads is not None:
        import capo_ec2.types.workloads_list

        out["workloads"] = capo_ec2.types.workloads_list.deserialize_ec2_query(
            child_workloads
        )
    child_memory_info = el.find("memoryInfo")
    if child_memory_info is not None:
        import capo_ec2.types.gpu_device_memory_info

        out["memory_info"] = (
            capo_ec2.types.gpu_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
