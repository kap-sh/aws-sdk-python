"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_id


class CreateContactResponse(TypedDict, closed=True):
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    contact_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the created contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "contact_arn" in value:
        out["ContactArn"] = value["contact_arn"]
    return out


def deserialize_json(data: dict) -> CreateContactResponse:
    out: CreateContactResponse = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    return out
