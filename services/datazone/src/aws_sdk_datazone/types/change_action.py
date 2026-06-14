"""Generated from Smithy shape ``com.amazonaws.datazone#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ChangeAction: TypeAlias = Literal[
    "PUBLISH",
    "UNPUBLISH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISH",
        "UNPUBLISH",
    )
)


def serialize_json(value: ChangeAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {data!r}")
    return cast(ChangeAction, data)
