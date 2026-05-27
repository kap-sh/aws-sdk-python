"""Generated from Smithy shape ``com.amazonaws.lambda#Operations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.operation

Operations: TypeAlias = list["aws_sdk_lambda.types.operation.Operation"]


# --- restJson1 ser/de ---
def serialize_json(value: Operations) -> list:
    import aws_sdk_lambda.types.operation

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Operations:
    import aws_sdk_lambda.types.operation

    out: Operations = []
    for item in data:
        out.append(aws_sdk_lambda.types.operation.deserialize_json(item))
    return out
