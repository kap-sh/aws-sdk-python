"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.volume_arn

VolumeArns: TypeAlias = list["aws_sdk_compute_optimizer.types.volume_arn.VolumeArn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VolumeArns:
    return list(data)
