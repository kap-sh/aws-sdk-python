"""Generated from Smithy shape ``com.amazonaws.lambda#OperationUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.operation_update

OperationUpdates: TypeAlias = list[
    "aws_sdk_lambda.types.operation_update.OperationUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationUpdates) -> list:
    import aws_sdk_lambda.types.operation_update

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.operation_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationUpdates:
    import aws_sdk_lambda.types.operation_update

    out: OperationUpdates = []
    for item in data:
        out.append(aws_sdk_lambda.types.operation_update.deserialize_json(item))
    return out
