"""Generated from Smithy shape ``com.amazonaws.connect#PhoneType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

PhoneType: TypeAlias = Literal[
    "SOFT_PHONE",
    "DESK_PHONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOFT_PHONE",
        "DESK_PHONE",
    )
)


def serialize_json(value: PhoneType) -> str:
    return value


def deserialize_json(data: str) -> PhoneType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneType value: {data!r}")
    return cast(PhoneType, data)
