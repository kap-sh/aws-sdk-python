"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Summaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.summary

Summaries: TypeAlias = list["aws_sdk_compute_optimizer.types.summary.Summary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summaries) -> list:
    import aws_sdk_compute_optimizer.types.summary

    out: list = []
    for item in value:
        out.append(aws_sdk_compute_optimizer.types.summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Summaries:
    import aws_sdk_compute_optimizer.types.summary

    out: Summaries = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.summary.deserialize_aws_json_1_0(item)
        )
    return out
