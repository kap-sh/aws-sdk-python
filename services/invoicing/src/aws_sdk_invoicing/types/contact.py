"""Generated from Smithy shape ``com.amazonaws.invoicing#Contact``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.email_string

class Contact(TypedDict):
    name: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The name of the contact person or role.</p>"""
    email: NotRequired["aws_sdk_invoicing.types.email_string.EmailString"]
    """<p>The email address of the contact person or role.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contact) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Email" in data:
        out["email"] = data["Email"]
    return out