"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#OperationType``."""

from typing import Literal, TypeAlias, cast

OperationType: TypeAlias = Literal[
    "INSERT",
    "MODIFY",
    "REMOVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationType:
    return cast(OperationType, data)
