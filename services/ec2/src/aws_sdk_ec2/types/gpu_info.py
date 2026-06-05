"""Generated from Smithy shape ``com.amazonaws.ec2#GpuInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_info_list
    import aws_sdk_ec2.types.total_gpu_memory


class GpuInfo(TypedDict):
    gpus: NotRequired["aws_sdk_ec2.types.gpu_device_info_list.GpuDeviceInfoList"]
    """<p>Describes the GPU accelerators for the instance type.</p>"""
    total_gpu_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_gpu_memory.totalGpuMemory"
    ]
    """<p>The total size of the memory for the GPU accelerators for the instance type, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GpuInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "gpus" in value:
        import aws_sdk_ec2.types.gpu_device_info_list

        aws_sdk_ec2.types.gpu_device_info_list.serialize_ec2_query(
            value["gpus"], pairs, f"{prefix}.Gpus"
        )
    if "total_gpu_memory_in_mi_b" in value:
        pairs.append(
            (f"{prefix}.TotalGpuMemoryInMiB", str(value["total_gpu_memory_in_mi_b"]))
        )


def deserialize_ec2_query(el: Element) -> GpuInfo:
    out: GpuInfo = {}  # type: ignore[typeddict-item]
    if el.find("Gpus") is not None:
        import aws_sdk_ec2.types.gpu_device_info_list

        out["gpus"] = aws_sdk_ec2.types.gpu_device_info_list.deserialize_ec2_query(
            el, "Gpus"
        )
    child_total_gpu_memory_in_mi_b = el.find("TotalGpuMemoryInMiB")
    if child_total_gpu_memory_in_mi_b is not None:
        out["total_gpu_memory_in_mi_b"] = int(child_total_gpu_memory_in_mi_b.text or "")
    return out
