"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Contact``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.contact_email
    import aws_sdk_partnercentral_benefits.types.contact_first_name
    import aws_sdk_partnercentral_benefits.types.contact_last_name
    import aws_sdk_partnercentral_benefits.types.contact_phone


class Contact(TypedDict):
    email: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contact_email.ContactEmail"
    ]
    """<p>The email address of the contact person.</p>"""
    first_name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contact_first_name.ContactFirstName"
    ]
    """<p>The first name of the contact person.</p>"""
    last_name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contact_last_name.ContactLastName"
    ]
    """<p>The last name of the contact person.</p>"""
    business_title: NotRequired["str"]
    """<p>The business title or role of the contact person within the organization.</p>"""
    phone: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contact_phone.ContactPhone"
    ]
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
