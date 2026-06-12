"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

PhoneNumberType: TypeAlias = Literal[
    "Local",
    "TollFree",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Local",
        "TollFree",
    )
)


def serialize_json(value: PhoneNumberType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberType value: {data!r}")
    return cast(PhoneNumberType, data)
