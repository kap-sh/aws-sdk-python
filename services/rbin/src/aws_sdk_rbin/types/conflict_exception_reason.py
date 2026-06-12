"""Generated from Smithy shape ``com.amazonaws.rbin#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

ConflictExceptionReason: TypeAlias = Literal["INVALID_RULE_STATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INVALID_RULE_STATE",))


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
