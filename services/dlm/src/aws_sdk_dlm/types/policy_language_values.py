"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyLanguageValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

PolicyLanguageValues: TypeAlias = Literal[
    "SIMPLIFIED",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIMPLIFIED",
        "STANDARD",
    )
)


def serialize_json(value: PolicyLanguageValues) -> str:
    return value


def deserialize_json(data: str) -> PolicyLanguageValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyLanguageValues value: {data!r}")
    return cast(PolicyLanguageValues, data)
