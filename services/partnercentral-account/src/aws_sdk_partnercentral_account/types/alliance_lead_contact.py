"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AllianceLeadContact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string


class AllianceLeadContact(TypedDict, closed=True):
    first_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The first name of the alliance lead contact person.</p>"""
    last_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The last name of the alliance lead contact person.</p>"""
    email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address of the alliance lead contact person.</p>"""
    business_title: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The business title or role of the alliance lead contact person.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AllianceLeadContact) -> dict:
    out: dict = {}
    out["FirstName"] = value["first_name"]
    out["LastName"] = value["last_name"]
    out["Email"] = value["email"]
    out["BusinessTitle"] = value["business_title"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AllianceLeadContact:
    out: AllianceLeadContact = {}  # type: ignore[typeddict-item]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    else:
        raise DeserializationError("AllianceLeadContact.first_name required")
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    else:
        raise DeserializationError("AllianceLeadContact.last_name required")
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("AllianceLeadContact.email required")
    if "BusinessTitle" in data:
        out["business_title"] = data["BusinessTitle"]
    else:
        raise DeserializationError("AllianceLeadContact.business_title required")
    return out
