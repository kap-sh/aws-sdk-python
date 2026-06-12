"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.email_address


class DeleteContactRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list from which the contact should be removed.</p>"""
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The contact's email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactRequest:
    out: DeleteContactRequest = {}  # type: ignore[typeddict-item]
    return out
