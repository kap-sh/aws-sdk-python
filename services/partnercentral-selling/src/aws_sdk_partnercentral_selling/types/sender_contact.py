"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SenderContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.job_title
    import aws_sdk_partnercentral_selling.types.name
    import aws_sdk_partnercentral_selling.types.phone_number
    import aws_sdk_partnercentral_selling.types.sender_contact_email


class SenderContact(TypedDict, closed=True):
    email: (
        "aws_sdk_partnercentral_selling.types.sender_contact_email.SenderContactEmail"
    )
    """<p>The sender-provided contact's email address associated with the <code>EngagementInvitation</code>.</p>"""
    first_name: NotRequired["aws_sdk_partnercentral_selling.types.name.Name"]
    """<p>The sender-provided contact's last name associated with the <code>EngagementInvitation</code>.</p>"""
    last_name: NotRequired["aws_sdk_partnercentral_selling.types.name.Name"]
    """<p>The sender-provided contact's first name associated with the <code>EngagementInvitation</code>.</p>"""
    business_title: NotRequired[
        "aws_sdk_partnercentral_selling.types.job_title.JobTitle"
    ]
    """<p>The sender-provided contact's title (job title or role) associated with the <code>EngagementInvitation</code>.</p>"""
    phone: NotRequired["aws_sdk_partnercentral_selling.types.phone_number.PhoneNumber"]
    """<p>The sender-provided contact's phone number associated with the <code>EngagementInvitation</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderContact) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_0(data: dict) -> SenderContact:
    out: SenderContact = {}  # type: ignore[typeddict-item]
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("SenderContact.email required")
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "BusinessTitle" in data:
        out["business_title"] = data["BusinessTitle"]
    if "Phone" in data:
        out["phone"] = data["Phone"]
    return out
