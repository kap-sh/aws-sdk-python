"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CpuVendorArchitectures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.cpu_vendor_architecture

CpuVendorArchitectures: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.cpu_vendor_architecture.CpuVendorArchitecture"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CpuVendorArchitectures) -> list:
    import aws_sdk_compute_optimizer.types.cpu_vendor_architecture

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.cpu_vendor_architecture.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CpuVendorArchitectures:
    import aws_sdk_compute_optimizer.types.cpu_vendor_architecture

    out: CpuVendorArchitectures = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.cpu_vendor_architecture.deserialize_aws_json_1_0(
                item
            )
        )
    return out
