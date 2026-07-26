"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressRecipientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_address_info

EmailAddressRecipientList: TypeAlias = list[
    "capo_connect.types.email_address_info.EmailAddressInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressRecipientList) -> list:
    import capo_connect.types.email_address_info

    out: list = []
    for item in value:
        out.append(capo_connect.types.email_address_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressRecipientList:
    import capo_connect.types.email_address_info

    out: EmailAddressRecipientList = []
    for item in data:
        out.append(capo_connect.types.email_address_info.deserialize_json(item))
    return out
