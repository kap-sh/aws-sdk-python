"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GlossaryTermStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: GlossaryTermStatus) -> str:
    return value


def deserialize_json(data: str) -> GlossaryTermStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlossaryTermStatus value: {data!r}")
    return cast(GlossaryTermStatus, data)
