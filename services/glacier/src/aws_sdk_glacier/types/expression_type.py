"""Generated from Smithy shape ``com.amazonaws.glacier#ExpressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

ExpressionType: TypeAlias = Literal["SQL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SQL",))


def serialize_json(value: ExpressionType) -> str:
    return value


def deserialize_json(data: str) -> ExpressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExpressionType value: {data!r}")
    return cast(ExpressionType, data)
