"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RecordFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

RecordFormat: TypeAlias = Literal[
    "STRING",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "JSON",
    )
)


def serialize_json(value: RecordFormat) -> str:
    return value


def deserialize_json(data: str) -> RecordFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordFormat value: {data!r}")
    return cast(RecordFormat, data)
