"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_address_id

EmailAddressIdList: TypeAlias = list[
    "capo_connect.types.email_address_id.EmailAddressId"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> EmailAddressIdList:
    return list(data)
