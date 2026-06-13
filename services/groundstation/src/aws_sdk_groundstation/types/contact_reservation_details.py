"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactReservationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class ContactReservationDetails(TypedDict):
    contact_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactReservationDetails) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> ContactReservationDetails:
    out: ContactReservationDetails = {}  # type: ignore[typeddict-item]
    if "contactId" in data:
        out["contact_id"] = data["contactId"]
    return out
