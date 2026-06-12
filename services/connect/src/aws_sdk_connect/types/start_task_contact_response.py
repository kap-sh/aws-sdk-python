"""Generated from Smithy shape ``com.amazonaws.connect#StartTaskContactResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id


class StartTaskContactResponse(TypedDict):
    contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The identifier of this contact within the Connect Customer instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTaskContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> StartTaskContactResponse:
    out: StartTaskContactResponse = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    return out
