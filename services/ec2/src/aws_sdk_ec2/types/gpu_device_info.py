"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_count
    import aws_sdk_ec2.types.gpu_device_manufacturer_name
    import aws_sdk_ec2.types.gpu_device_memory_info
    import aws_sdk_ec2.types.gpu_device_name
    import aws_sdk_ec2.types.gpu_partition_size
    import aws_sdk_ec2.types.logical_gpu_count
    import aws_sdk_ec2.types.workloads_list


class GpuDeviceInfo(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ec2.types.gpu_device_name.GpuDeviceName"]
    """<p>The name of the GPU accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.gpu_device_manufacturer_name.GpuDeviceManufacturerName"
    ]
    """<p>The manufacturer of the GPU accelerator.</p>"""
    count: NotRequired["aws_sdk_ec2.types.gpu_device_count.GpuDeviceCount"]
    """<p>The number of GPUs for the instance type.</p>"""
    logical_gpu_count: NotRequired[
        "aws_sdk_ec2.types.logical_gpu_count.LogicalGpuCount"
    ]
    """<p>Total number of GPU devices of this type.</p>"""
    gpu_partition_size: NotRequired[
        "aws_sdk_ec2.types.gpu_partition_size.GpuPartitionSize"
    ]
    """<p>The size of each GPU as a fraction of a full GPU, between 0 (excluded) and 1 (included).</p>"""
    workloads: NotRequired["aws_sdk_ec2.types.workloads_list.WorkloadsList"]
    """<p>A list of workload types this GPU supports.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.gpu_device_memory_info.GpuDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the GPU accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GpuDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "manufacturer" in value:
        pairs.append((f"{prefix}.Manufacturer", str(value["manufacturer"])))
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "logical_gpu_count" in value:
        pairs.append((f"{prefix}.LogicalGpuCount", str(value["logical_gpu_count"])))
    if "gpu_partition_size" in value:
        pairs.append((f"{prefix}.GpuPartitionSize", str(value["gpu_partition_size"])))
    if "workloads" in value:
        import aws_sdk_ec2.types.workloads_list

        aws_sdk_ec2.types.workloads_list.serialize_ec2_query(
            value["workloads"], pairs, f"{prefix}.WorkloadSet"
        )
    if "memory_info" in value:
        import aws_sdk_ec2.types.gpu_device_memory_info

        aws_sdk_ec2.types.gpu_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{prefix}.MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> GpuDeviceInfo:
    out: GpuDeviceInfo = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_manufacturer = el.find("Manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_logical_gpu_count = el.find("LogicalGpuCount")
    if child_logical_gpu_count is not None:
        out["logical_gpu_count"] = int(child_logical_gpu_count.text or "")
    child_gpu_partition_size = el.find("GpuPartitionSize")
    if child_gpu_partition_size is not None:
        out["gpu_partition_size"] = float(child_gpu_partition_size.text or "")
    if el.find("WorkloadSet") is not None:
        import aws_sdk_ec2.types.workloads_list

        out["workloads"] = aws_sdk_ec2.types.workloads_list.deserialize_ec2_query(
            el, "WorkloadSet"
        )
    child_memory_info = el.find("MemoryInfo")
    if child_memory_info is not None:
        import aws_sdk_ec2.types.gpu_device_memory_info

        out["memory_info"] = (
            aws_sdk_ec2.types.gpu_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
