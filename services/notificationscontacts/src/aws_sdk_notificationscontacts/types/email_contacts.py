"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#EmailContacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact

EmailContacts: TypeAlias = list[
    "aws_sdk_notificationscontacts.types.email_contact.EmailContact"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailContacts) -> list:
    import aws_sdk_notificationscontacts.types.email_contact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_notificationscontacts.types.email_contact.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EmailContacts:
    import aws_sdk_notificationscontacts.types.email_contact

    out: EmailContacts = []
    for item in data:
        out.append(
            aws_sdk_notificationscontacts.types.email_contact.deserialize_json(item)
        )
    return out
