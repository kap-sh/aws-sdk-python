"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberOrderStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PhoneNumberOrderStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberOrderStatus:
    return cast(PhoneNumberOrderStatus, data)
