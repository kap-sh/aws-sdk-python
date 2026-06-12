"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

MetricName: TypeAlias = Literal[
    "Cpu",
    "Memory",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "DISK_READ_OPS_PER_SECOND",
    "DISK_WRITE_OPS_PER_SECOND",
    "DISK_READ_BYTES_PER_SECOND",
    "DISK_WRITE_BYTES_PER_SECOND",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
    "GPU_PERCENTAGE",
    "GPU_MEMORY_PERCENTAGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cpu",
        "Memory",
        "EBS_READ_OPS_PER_SECOND",
        "EBS_WRITE_OPS_PER_SECOND",
        "EBS_READ_BYTES_PER_SECOND",
        "EBS_WRITE_BYTES_PER_SECOND",
        "DISK_READ_OPS_PER_SECOND",
        "DISK_WRITE_OPS_PER_SECOND",
        "DISK_READ_BYTES_PER_SECOND",
        "DISK_WRITE_BYTES_PER_SECOND",
        "NETWORK_IN_BYTES_PER_SECOND",
        "NETWORK_OUT_BYTES_PER_SECOND",
        "NETWORK_PACKETS_IN_PER_SECOND",
        "NETWORK_PACKETS_OUT_PER_SECOND",
        "GPU_PERCENTAGE",
        "GPU_MEMORY_PERCENTAGE",
    )
)


def serialize_aws_json_1_0(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricName value: {data!r}")
    return cast(MetricName, data)
