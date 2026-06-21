"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CpuVendorArchitecture``."""

from typing import Literal, TypeAlias, cast

CpuVendorArchitecture: TypeAlias = Literal[
    "AWS_ARM64",
    "CURRENT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CpuVendorArchitecture) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CpuVendorArchitecture:
    return cast(CpuVendorArchitecture, data)
