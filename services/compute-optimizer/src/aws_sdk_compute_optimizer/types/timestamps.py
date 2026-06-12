"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Timestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.timestamp

Timestamps: TypeAlias = list["aws_sdk_compute_optimizer.types.timestamp.Timestamp"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timestamps) -> list:
    import aws_sdk_compute_optimizer.types.timestamp

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.timestamp.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Timestamps:
    import aws_sdk_compute_optimizer.types.timestamp

    out: Timestamps = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(item)
        )
    return out
