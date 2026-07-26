"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionalOperator``."""

from typing import Literal, TypeAlias, cast

ConditionalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConditionalOperator:
    return cast(ConditionalOperator, data)
