"""Generated from Smithy shape ``com.amazonaws.connect#StartOutboundEmailContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id


class StartOutboundEmailContactResponse(TypedDict, closed=True):
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutboundEmailContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> StartOutboundEmailContactResponse:
    out: StartOutboundEmailContactResponse = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    return out
