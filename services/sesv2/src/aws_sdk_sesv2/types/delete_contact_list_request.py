"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteContactListRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name


class DeleteContactListRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactListRequest:
    out: DeleteContactListRequest = {}  # type: ignore[typeddict-item]
    return out
