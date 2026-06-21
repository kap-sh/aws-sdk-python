"""Generated from Smithy shape ``com.amazonaws.swf#StartLambdaFunctionFailedCause``."""

from typing import Literal, TypeAlias, cast

StartLambdaFunctionFailedCause: TypeAlias = Literal["ASSUME_ROLE_FAILED",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartLambdaFunctionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartLambdaFunctionFailedCause:
    return cast(StartLambdaFunctionFailedCause, data)
