"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Operator``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.operator_value

Operator: TypeAlias = list["aws_sdk_cloudtrail.types.operator_value.OperatorValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operator) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Operator:
    return list(data)
