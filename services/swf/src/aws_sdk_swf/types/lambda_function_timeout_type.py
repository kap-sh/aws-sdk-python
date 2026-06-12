"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionTimeoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

LambdaFunctionTimeoutType: TypeAlias = Literal["START_TO_CLOSE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("START_TO_CLOSE",))


def serialize_aws_json_1_0(value: LambdaFunctionTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionTimeoutType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaFunctionTimeoutType value: {data!r}")
    return cast(LambdaFunctionTimeoutType, data)
