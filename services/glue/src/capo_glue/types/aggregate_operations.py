"""Generated from Smithy shape ``com.amazonaws.glue#AggregateOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.aggregate_operation

AggregateOperations: TypeAlias = list[
    "capo_glue.types.aggregate_operation.AggregateOperation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateOperations) -> list:
    import capo_glue.types.aggregate_operation

    out: list = []
    for item in value:
        out.append(capo_glue.types.aggregate_operation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateOperations:
    import capo_glue.types.aggregate_operation

    out: AggregateOperations = []
    for item in data:
        out.append(capo_glue.types.aggregate_operation.deserialize_aws_json_1_1(item))
    return out
