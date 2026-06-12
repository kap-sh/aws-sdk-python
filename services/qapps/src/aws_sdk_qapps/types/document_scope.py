"""Generated from Smithy shape ``com.amazonaws.qapps#DocumentScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

DocumentScope: TypeAlias = Literal[
    "APPLICATION",
    "SESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION",
        "SESSION",
    )
)


def serialize_json(value: DocumentScope) -> str:
    return value


def deserialize_json(data: str) -> DocumentScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentScope value: {data!r}")
    return cast(DocumentScope, data)
