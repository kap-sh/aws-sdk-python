"""Generated from Smithy shape ``com.amazonaws.backup#ConditionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ConditionType: TypeAlias = Literal["STRINGEQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STRINGEQUALS",))


def serialize_json(value: ConditionType) -> str:
    return value


def deserialize_json(data: str) -> ConditionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionType value: {data!r}")
    return cast(ConditionType, data)
