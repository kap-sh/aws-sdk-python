"""Generated from Smithy shape ``com.amazonaws.sesv2#ListContactListsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.list_of_contact_lists
    import aws_sdk_sesv2.types.next_token


class ListContactListsResponse(TypedDict):
    contact_lists: NotRequired[
        "aws_sdk_sesv2.types.list_of_contact_lists.ListOfContactLists"
    ]
    """<p>The available contact lists.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional contact lists available to be listed. Copy this token to a subsequent call to <code>ListContactLists</code> with the same parameters to retrieve the next page of contact lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactListsResponse) -> dict:
    out: dict = {}
    if "contact_lists" in value:
        import aws_sdk_sesv2.types.list_of_contact_lists

        out["ContactLists"] = aws_sdk_sesv2.types.list_of_contact_lists.serialize_json(
            value["contact_lists"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactListsResponse:
    out: ListContactListsResponse = {}  # type: ignore[typeddict-item]
    if "ContactLists" in data:
        import aws_sdk_sesv2.types.list_of_contact_lists

        out["contact_lists"] = (
            aws_sdk_sesv2.types.list_of_contact_lists.deserialize_json(
                data["ContactLists"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
