"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.contact_email
    import capo_partnercentral_benefits.types.contact_first_name
    import capo_partnercentral_benefits.types.contact_last_name
    import capo_partnercentral_benefits.types.contact_phone


class Contact(TypedDict, closed=True):
    email: NotRequired["capo_partnercentral_benefits.types.contact_email.ContactEmail"]
    """<p>The email address of the contact person.</p>"""
    first_name: NotRequired[
        "capo_partnercentral_benefits.types.contact_first_name.ContactFirstName"
    ]
    """<p>The first name of the contact person.</p>"""
    last_name: NotRequired[
        "capo_partnercentral_benefits.types.contact_last_name.ContactLastName"
    ]
    """<p>The last name of the contact person.</p>"""
    business_title: NotRequired["str"]
    """<p>The business title or role of the contact person within the organization.</p>"""
    phone: NotRequired["capo_partnercentral_benefits.types.contact_phone.ContactPhone"]
    """<p>The phone number of the contact person.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contact) -> dict:
    out: dict = {}
    if "email" in value:
        out["Email"] = value["email"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "business_title" in value:
        out["BusinessTitle"] = value["business_title"]
    if "phone" in value:
        out["Phone"] = value["phone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "Email" in data:
        out["email"] = data["Email"]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "BusinessTitle" in data:
        out["business_title"] = data["BusinessTitle"]
    if "Phone" in data:
        out["phone"] = data["Phone"]
    return out
