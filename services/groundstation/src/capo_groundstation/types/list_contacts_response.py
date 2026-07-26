"""Generated from Smithy shape ``com.amazonaws.groundstation#ListContactsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.contact_list
    import capo_groundstation.types.pagination_token


class ListContactsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token returned in the response of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>"""
    contact_list: NotRequired["capo_groundstation.types.contact_list.ContactList"]
    """<p>List of contacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "contact_list" in value:
        import capo_groundstation.types.contact_list

        out["contactList"] = capo_groundstation.types.contact_list.serialize_json(
            value["contact_list"]
        )
    return out


def deserialize_json(data: dict) -> ListContactsResponse:
    out: ListContactsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "contactList" in data:
        import capo_groundstation.types.contact_list

        out["contact_list"] = capo_groundstation.types.contact_list.deserialize_json(
            data["contactList"]
        )
    return out
