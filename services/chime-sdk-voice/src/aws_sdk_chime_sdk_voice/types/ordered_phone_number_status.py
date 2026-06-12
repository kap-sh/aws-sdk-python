"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OrderedPhoneNumberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

OrderedPhoneNumberStatus: TypeAlias = Literal[
    "Processing",
    "Acquired",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Processing",
        "Acquired",
        "Failed",
    )
)


def serialize_json(value: OrderedPhoneNumberStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderedPhoneNumberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderedPhoneNumberStatus value: {data!r}")
    return cast(OrderedPhoneNumberStatus, data)
