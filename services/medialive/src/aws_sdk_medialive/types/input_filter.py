"""Generated from Smithy shape ``com.amazonaws.medialive#InputFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Filter"""
InputFilter: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
    "FORCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "DISABLED",
        "FORCED",
    )
)


def serialize_json(value: InputFilter) -> str:
    return value


def deserialize_json(data: str) -> InputFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputFilter value: {data!r}")
    return cast(InputFilter, data)
