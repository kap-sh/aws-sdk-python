"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

AttributeEntityType: TypeAlias = Literal[
    "ASSET",
    "LISTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "LISTING",
    )
)


def serialize_json(value: AttributeEntityType) -> str:
    return value


def deserialize_json(data: str) -> AttributeEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeEntityType value: {data!r}")
    return cast(AttributeEntityType, data)
