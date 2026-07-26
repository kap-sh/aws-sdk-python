"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionTimeoutType``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionTimeoutType: TypeAlias = Literal["START_TO_CLOSE",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionTimeoutType:
    return cast(LambdaFunctionTimeoutType, data)
