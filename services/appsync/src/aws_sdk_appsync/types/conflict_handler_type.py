"""Generated from Smithy shape ``com.amazonaws.appsync#ConflictHandlerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ConflictHandlerType: TypeAlias = Literal[
    "OPTIMISTIC_CONCURRENCY",
    "LAMBDA",
    "AUTOMERGE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPTIMISTIC_CONCURRENCY",
        "LAMBDA",
        "AUTOMERGE",
        "NONE",
    )
)


def serialize_json(value: ConflictHandlerType) -> str:
    return value


def deserialize_json(data: str) -> ConflictHandlerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictHandlerType value: {data!r}")
    return cast(ConflictHandlerType, data)
