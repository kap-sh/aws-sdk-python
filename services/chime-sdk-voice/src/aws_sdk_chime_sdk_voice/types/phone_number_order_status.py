"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberOrderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

PhoneNumberOrderStatus: TypeAlias = Literal[
    "Processing",
    "Successful",
    "Failed",
    "Partial",
    "PendingDocuments",
    "Submitted",
    "FOC",
    "ChangeRequested",
    "Exception",
    "CancelRequested",
    "Cancelled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Processing",
        "Successful",
        "Failed",
        "Partial",
        "PendingDocuments",
        "Submitted",
        "FOC",
        "ChangeRequested",
        "Exception",
        "CancelRequested",
        "Cancelled",
    )
)


def serialize_json(value: PhoneNumberOrderStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberOrderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberOrderStatus value: {data!r}")
    return cast(PhoneNumberOrderStatus, data)
