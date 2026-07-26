"""Generated from Smithy shape ``com.amazonaws.securityagent#LambdaFunctionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.lambda_function_arn

LambdaFunctionArns: TypeAlias = list[
    "capo_securityagent.types.lambda_function_arn.LambdaFunctionArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionArns) -> list:
    return list(value)


def deserialize_json(data: list) -> LambdaFunctionArns:
    return list(data)
