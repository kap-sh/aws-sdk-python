"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FunctionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.function_arn

FunctionArns: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.function_arn.FunctionArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FunctionArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FunctionArns:
    return list(data)
