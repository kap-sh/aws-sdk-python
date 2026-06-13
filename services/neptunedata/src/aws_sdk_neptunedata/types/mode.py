"""Generated from Smithy shape ``com.amazonaws.neptunedata#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

Mode: TypeAlias = Literal[
    "RESUME",
    "NEW",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESUME",
        "NEW",
        "AUTO",
    )
)


def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {data!r}")
    return cast(Mode, data)
