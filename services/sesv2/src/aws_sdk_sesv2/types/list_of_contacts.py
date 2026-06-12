"""Generated from Smithy shape ``com.amazonaws.sesv2#ListOfContacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact

ListOfContacts: TypeAlias = list["aws_sdk_sesv2.types.contact.Contact"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfContacts) -> list:
    import aws_sdk_sesv2.types.contact

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.contact.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfContacts:
    import aws_sdk_sesv2.types.contact

    out: ListOfContacts = []
    for item in data:
        out.append(aws_sdk_sesv2.types.contact.deserialize_json(item))
    return out
