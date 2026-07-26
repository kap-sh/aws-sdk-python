"""Generated from Smithy shape ``com.amazonaws.rbin#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal["INVALID_RULE_STATE",]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
