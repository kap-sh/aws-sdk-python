"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberOrderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

PhoneNumberOrderStatus: TypeAlias = Literal[
    "Processing",
    "Successful",
    "Failed",
    "Partial",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Processing",
        "Successful",
        "Failed",
        "Partial",
    )
)


def serialize_json(value: PhoneNumberOrderStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberOrderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberOrderStatus value: {data!r}")
    return cast(PhoneNumberOrderStatus, data)
