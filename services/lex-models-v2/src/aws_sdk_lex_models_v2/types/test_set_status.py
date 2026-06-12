"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestSetStatus: TypeAlias = Literal[
    "Importing",
    "PendingAnnotation",
    "Deleting",
    "ValidationError",
    "Ready",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Importing",
        "PendingAnnotation",
        "Deleting",
        "ValidationError",
        "Ready",
    )
)


def serialize_json(value: TestSetStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestSetStatus value: {data!r}")
    return cast(TestSetStatus, data)
