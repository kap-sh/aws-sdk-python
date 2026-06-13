"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ConflictExceptionReason: TypeAlias = Literal["CONCURRENT_MODIFICATION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONCURRENT_MODIFICATION",))


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
