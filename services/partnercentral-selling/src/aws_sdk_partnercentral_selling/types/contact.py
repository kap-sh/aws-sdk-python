"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Contact``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.email
    import aws_sdk_partnercentral_selling.types.job_title
    import aws_sdk_partnercentral_selling.types.name
    import aws_sdk_partnercentral_selling.types.phone_number


class Contact(TypedDict):
    email: NotRequired["aws_sdk_partnercentral_selling.types.email.Email"]
    """<p>The contact's email address associated with the <code>Opportunity</code>.</p>"""
    first_name: NotRequired["aws_sdk_partnercentral_selling.types.name.Name"]
    """<p>The contact's first name associated with the <code>Opportunity</code>.</p>"""
    last_name: NotRequired["aws_sdk_partnercentral_selling.types.name.Name"]
    """<p>The contact's last name associated with the <code>Opportunity</code>.</p>"""
    business_title: NotRequired[
        "aws_sdk_partnercentral_selling.types.job_title.JobTitle"
    ]
    """<p>The partner contact's title (job title or role) associated with the <code>Opportunity</code>. <code>BusinessTitle</code> supports either <code>PartnerAccountManager</code> or <code>OpportunityOwner</code>.</p>"""
    phone: NotRequired["aws_sdk_partnercentral_selling.types.phone_number.PhoneNumber"]
    """<p>The contact's phone number associated with the <code>Opportunity</code>.</p>"""


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
