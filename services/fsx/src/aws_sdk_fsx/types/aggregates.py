"""Generated from Smithy shape ``com.amazonaws.fsx#Aggregates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aggregate

Aggregates: TypeAlias = list["aws_sdk_fsx.types.aggregate.Aggregate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Aggregates) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Aggregates:
    return list(data)
