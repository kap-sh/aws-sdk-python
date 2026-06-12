"""Generated from Smithy shape ``com.amazonaws.workdocs#BooleanEnumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

BooleanEnumType: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
    )
)


def serialize_json(value: BooleanEnumType) -> str:
    return value


def deserialize_json(data: str) -> BooleanEnumType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BooleanEnumType value: {data!r}")
    return cast(BooleanEnumType, data)
