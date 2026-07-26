"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.email_address

EmailAddressList: TypeAlias = list["capo_sesv2.types.email_address.EmailAddress"]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> EmailAddressList:
    return list(data)
