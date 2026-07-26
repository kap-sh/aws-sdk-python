"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal["CONCURRENT_MODIFICATION",]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
