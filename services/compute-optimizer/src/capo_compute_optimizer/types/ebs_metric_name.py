"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSMetricName``."""

from typing import Literal, TypeAlias, cast

EBSMetricName: TypeAlias = Literal[
    "VolumeReadOpsPerSecond",
    "VolumeWriteOpsPerSecond",
    "VolumeReadBytesPerSecond",
    "VolumeWriteBytesPerSecond",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSMetricName:
    return cast(EBSMetricName, data)
