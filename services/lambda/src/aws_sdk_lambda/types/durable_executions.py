"""Generated from Smithy shape ``com.amazonaws.lambda#DurableExecutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.execution

DurableExecutions: TypeAlias = list["aws_sdk_lambda.types.execution.Execution"]


# --- restJson1 ser/de ---
def serialize_json(value: DurableExecutions) -> list:
    import aws_sdk_lambda.types.execution

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> DurableExecutions:
    import aws_sdk_lambda.types.execution

    out: DurableExecutions = []
    for item in data:
        out.append(aws_sdk_lambda.types.execution.deserialize_json(item))
    return out
