"""Generated from Smithy shape ``com.amazonaws.shield#EmergencyContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.contact_notes
    import capo_shield.types.email_address
    import capo_shield.types.phone_number


class EmergencyContact(TypedDict, closed=True):
    email_address: "capo_shield.types.email_address.EmailAddress"
    """<p>The email address for the contact.</p>"""
    phone_number: NotRequired["capo_shield.types.phone_number.PhoneNumber"]
    """<p>The phone number for the contact.</p>"""
    contact_notes: NotRequired["capo_shield.types.contact_notes.ContactNotes"]
    """<p>Additional notes regarding the contact. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmergencyContact) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "contact_notes" in value:
        out["ContactNotes"] = value["contact_notes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmergencyContact:
    out: EmergencyContact = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("EmergencyContact.email_address required")
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "ContactNotes" in data:
        out["contact_notes"] = data["ContactNotes"]
    return out
