"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_arn

FunctionArnList: TypeAlias = list["capo_lambda.types.function_arn.FunctionArn"]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FunctionArnList:
    return list(data)
