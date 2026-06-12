"""Generated from Smithy shape ``com.amazonaws.glue#AggregateOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.aggregate_operation

AggregateOperations: TypeAlias = list[
    "aws_sdk_glue.types.aggregate_operation.AggregateOperation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateOperations) -> list:
    import aws_sdk_glue.types.aggregate_operation

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.aggregate_operation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateOperations:
    import aws_sdk_glue.types.aggregate_operation

    out: AggregateOperations = []
    for item in data:
        out.append(
            aws_sdk_glue.types.aggregate_operation.deserialize_aws_json_1_1(item)
        )
    return out
