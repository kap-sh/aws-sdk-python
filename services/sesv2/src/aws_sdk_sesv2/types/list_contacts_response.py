"""Generated from Smithy shape ``com.amazonaws.sesv2#ListContactsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.list_of_contacts
    import aws_sdk_sesv2.types.next_token


class ListContactsResponse(TypedDict, closed=True):
    contacts: NotRequired["aws_sdk_sesv2.types.list_of_contacts.ListOfContacts"]
    """<p>The contacts present in a specific contact list.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional contacts available to be listed. Copy this token to a subsequent call to <code>ListContacts</code> with the same parameters to retrieve the next page of contacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsResponse) -> dict:
    out: dict = {}
    if "contacts" in value:
        import aws_sdk_sesv2.types.list_of_contacts

        out["Contacts"] = aws_sdk_sesv2.types.list_of_contacts.serialize_json(
            value["contacts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactsResponse:
    out: ListContactsResponse = {}  # type: ignore[typeddict-item]
    if "Contacts" in data:
        import aws_sdk_sesv2.types.list_of_contacts

        out["contacts"] = aws_sdk_sesv2.types.list_of_contacts.deserialize_json(
            data["Contacts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
