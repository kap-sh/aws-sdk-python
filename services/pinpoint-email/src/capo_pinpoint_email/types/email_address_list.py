"""Generated from Smithy shape ``com.amazonaws.pinpointemail#EmailAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.email_address

EmailAddressList: TypeAlias = list[
    "capo_pinpoint_email.types.email_address.EmailAddress"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> EmailAddressList:
    return list(data)
