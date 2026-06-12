"""Generated from Smithy shape ``com.amazonaws.swf#StartLambdaFunctionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

StartLambdaFunctionFailedCause: TypeAlias = Literal["ASSUME_ROLE_FAILED",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSUME_ROLE_FAILED",))


def serialize_aws_json_1_0(value: StartLambdaFunctionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartLambdaFunctionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StartLambdaFunctionFailedCause value: {data!r}"
        )
    return cast(StartLambdaFunctionFailedCause, data)
