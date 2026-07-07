"""Generated from Smithy shape ``com.amazonaws.connect#CreatePersistentContactAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id


class CreatePersistentContactAssociationResponse(TypedDict, closed=True):
    continued_from_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The contactId from which a persistent chat session is started. This field is populated only for persistent chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePersistentContactAssociationResponse) -> dict:
    out: dict = {}
    if "continued_from_contact_id" in value:
        out["ContinuedFromContactId"] = value["continued_from_contact_id"]
    return out


def deserialize_json(data: dict) -> CreatePersistentContactAssociationResponse:
    out: CreatePersistentContactAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ContinuedFromContactId" in data:
        out["continued_from_contact_id"] = data["ContinuedFromContactId"]
    return out
