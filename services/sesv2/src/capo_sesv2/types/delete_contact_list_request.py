"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteContactListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name


class DeleteContactListRequest(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactListRequest:
    out: DeleteContactListRequest = {}  # type: ignore[typeddict-item]
    return out
