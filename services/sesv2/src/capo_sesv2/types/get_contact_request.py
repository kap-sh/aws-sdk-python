"""Generated from Smithy shape ``com.amazonaws.sesv2#GetContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.email_address


class GetContactRequest(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list to which the contact belongs.</p>"""
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The contact's email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContactRequest:
    out: GetContactRequest = {}  # type: ignore[typeddict-item]
    return out
