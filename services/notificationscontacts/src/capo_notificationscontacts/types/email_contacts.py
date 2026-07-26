"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#EmailContacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact

EmailContacts: TypeAlias = list[
    "capo_notificationscontacts.types.email_contact.EmailContact"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailContacts) -> list:
    import capo_notificationscontacts.types.email_contact

    out: list = []
    for item in value:
        out.append(capo_notificationscontacts.types.email_contact.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailContacts:
    import capo_notificationscontacts.types.email_contact

    out: EmailContacts = []
    for item in data:
        out.append(
            capo_notificationscontacts.types.email_contact.deserialize_json(item)
        )
    return out
