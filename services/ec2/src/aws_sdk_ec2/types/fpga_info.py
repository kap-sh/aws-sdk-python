"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_device_info_list
    import aws_sdk_ec2.types.total_fpga_memory


class FpgaInfo(TypedDict):
    fpgas: NotRequired["aws_sdk_ec2.types.fpga_device_info_list.FpgaDeviceInfoList"]
    """<p>Describes the FPGAs for the instance type.</p>"""
    total_fpga_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_fpga_memory.totalFpgaMemory"
    ]
    """<p>The total memory of all FPGA accelerators for the instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpgas" in value:
        import aws_sdk_ec2.types.fpga_device_info_list

        aws_sdk_ec2.types.fpga_device_info_list.serialize_ec2_query(
            value["fpgas"], pairs, f"{prefix}.Fpgas"
        )
    if "total_fpga_memory_in_mi_b" in value:
        pairs.append(
            (f"{prefix}.TotalFpgaMemoryInMiB", str(value["total_fpga_memory_in_mi_b"]))
        )


def deserialize_ec2_query(el: Element) -> FpgaInfo:
    out: FpgaInfo = {}  # type: ignore[typeddict-item]
    if el.find("Fpgas") is not None:
        import aws_sdk_ec2.types.fpga_device_info_list

        out["fpgas"] = aws_sdk_ec2.types.fpga_device_info_list.deserialize_ec2_query(
            el, "Fpgas"
        )
    child_total_fpga_memory_in_mi_b = el.find("TotalFpgaMemoryInMiB")
    if child_total_fpga_memory_in_mi_b is not None:
        out["total_fpga_memory_in_mi_b"] = int(
            child_total_fpga_memory_in_mi_b.text or ""
        )
    return out
