"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#CreateEmailContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact_arn


class CreateEmailContactResponse(TypedDict, closed=True):
    arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailContactResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateEmailContactResponse:
    out: CreateEmailContactResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateEmailContactResponse.arn required")
    return out
