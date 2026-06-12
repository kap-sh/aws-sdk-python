"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Gpus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.gpu

Gpus: TypeAlias = list["aws_sdk_compute_optimizer.types.gpu.Gpu"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Gpus) -> list:
    import aws_sdk_compute_optimizer.types.gpu

    out: list = []
    for item in value:
        out.append(aws_sdk_compute_optimizer.types.gpu.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Gpus:
    import aws_sdk_compute_optimizer.types.gpu

    out: Gpus = []
    for item in data:
        out.append(aws_sdk_compute_optimizer.types.gpu.deserialize_aws_json_1_0(item))
    return out
