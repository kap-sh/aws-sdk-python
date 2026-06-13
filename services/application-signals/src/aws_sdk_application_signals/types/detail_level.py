"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DetailLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

DetailLevel: TypeAlias = Literal[
    "BRIEF",
    "DETAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BRIEF",
        "DETAILED",
    )
)


def serialize_json(value: DetailLevel) -> str:
    return value


def deserialize_json(data: str) -> DetailLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailLevel value: {data!r}")
    return cast(DetailLevel, data)
