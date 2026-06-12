"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EBSMetricName: TypeAlias = Literal[
    "VolumeReadOpsPerSecond",
    "VolumeWriteOpsPerSecond",
    "VolumeReadBytesPerSecond",
    "VolumeWriteBytesPerSecond",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VolumeReadOpsPerSecond",
        "VolumeWriteOpsPerSecond",
        "VolumeReadBytesPerSecond",
        "VolumeWriteBytesPerSecond",
    )
)


def serialize_aws_json_1_0(value: EBSMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EBSMetricName value: {data!r}")
    return cast(EBSMetricName, data)
