"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#GetEmailContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact


class GetEmailContactResponse(TypedDict, closed=True):
    email_contact: "capo_notificationscontacts.types.email_contact.EmailContact"
    """<p>The email contact for the provided email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailContactResponse) -> dict:
    out: dict = {}
    import capo_notificationscontacts.types.email_contact

    out["emailContact"] = capo_notificationscontacts.types.email_contact.serialize_json(
        value["email_contact"]
    )
    return out


def deserialize_json(data: dict) -> GetEmailContactResponse:
    out: GetEmailContactResponse = {}  # type: ignore[typeddict-item]
    if "emailContact" in data:
        import capo_notificationscontacts.types.email_contact

        out["email_contact"] = (
            capo_notificationscontacts.types.email_contact.deserialize_json(
                data["emailContact"]
            )
        )
    else:
        raise DeserializationError("GetEmailContactResponse.email_contact required")
    return out
