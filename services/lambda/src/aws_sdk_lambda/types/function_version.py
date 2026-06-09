"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

FunctionVersion: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: FunctionVersion) -> str:
    return value


def deserialize_json(data: str) -> FunctionVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionVersion value: {data!r}")
    return cast(FunctionVersion, data)
