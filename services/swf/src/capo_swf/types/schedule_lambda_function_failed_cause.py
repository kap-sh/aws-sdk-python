"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleLambdaFunctionFailedCause``."""

from typing import Literal, TypeAlias, cast

ScheduleLambdaFunctionFailedCause: TypeAlias = Literal[
    "ID_ALREADY_IN_USE",
    "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
    "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
    "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleLambdaFunctionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduleLambdaFunctionFailedCause:
    return cast(ScheduleLambdaFunctionFailedCause, data)
