"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ListEmailContactsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contacts


class ListEmailContactsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    email_contacts: "capo_notificationscontacts.types.email_contacts.EmailContacts"
    """<p>A list of email contacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailContactsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notificationscontacts.types.email_contacts

    out["emailContacts"] = (
        capo_notificationscontacts.types.email_contacts.serialize_json(
            value["email_contacts"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListEmailContactsResponse:
    out: ListEmailContactsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "emailContacts" in data:
        import capo_notificationscontacts.types.email_contacts

        out["email_contacts"] = (
            capo_notificationscontacts.types.email_contacts.deserialize_json(
                data["emailContacts"]
            )
        )
    else:
        raise DeserializationError("ListEmailContactsResponse.email_contacts required")
    return out
