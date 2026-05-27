"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionResponseType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

FunctionResponseType: TypeAlias = Literal["ReportBatchItemFailures",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ReportBatchItemFailures",))


def serialize_json(value: FunctionResponseType) -> str:
    return value


def deserialize_json(data: str) -> FunctionResponseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionResponseType value: {data!r}")
    return cast(FunctionResponseType, data)
