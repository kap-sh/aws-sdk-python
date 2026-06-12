"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.tag

Tags: TypeAlias = list["aws_sdk_compute_optimizer.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import aws_sdk_compute_optimizer.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_compute_optimizer.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import aws_sdk_compute_optimizer.types.tag

    out: Tags = []
    for item in data:
        out.append(aws_sdk_compute_optimizer.types.tag.deserialize_aws_json_1_0(item))
    return out
