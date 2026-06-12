"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CpuVendorArchitecture``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

CpuVendorArchitecture: TypeAlias = Literal[
    "AWS_ARM64",
    "CURRENT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_ARM64",
        "CURRENT",
    )
)


def serialize_aws_json_1_0(value: CpuVendorArchitecture) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CpuVendorArchitecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CpuVendorArchitecture value: {data!r}")
    return cast(CpuVendorArchitecture, data)
