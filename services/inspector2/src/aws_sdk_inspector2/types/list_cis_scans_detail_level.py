"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansDetailLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

ListCisScansDetailLevel: TypeAlias = Literal[
    "ORGANIZATION",
    "MEMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORGANIZATION",
        "MEMBER",
    )
)


def serialize_json(value: ListCisScansDetailLevel) -> str:
    return value


def deserialize_json(data: str) -> ListCisScansDetailLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListCisScansDetailLevel value: {data!r}")
    return cast(ListCisScansDetailLevel, data)
