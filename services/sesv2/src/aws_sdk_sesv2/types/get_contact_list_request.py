"""Generated from Smithy shape ``com.amazonaws.sesv2#GetContactListRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name


class GetContactListRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContactListRequest:
    out: GetContactListRequest = {}  # type: ignore[typeddict-item]
    return out
