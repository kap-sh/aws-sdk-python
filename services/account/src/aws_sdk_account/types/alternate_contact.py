"""Generated from Smithy shape ``com.amazonaws.account#AlternateContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_account.types.alternate_contact_type
    import aws_sdk_account.types.email_address
    import aws_sdk_account.types.name
    import aws_sdk_account.types.phone_number
    import aws_sdk_account.types.title


class AlternateContact(TypedDict, closed=True):
    name: NotRequired["aws_sdk_account.types.name.Name"]
    """<p>The name associated with this alternate contact.</p>"""
    title: NotRequired["aws_sdk_account.types.title.Title"]
    """<p>The title associated with this alternate contact.</p>"""
    email_address: NotRequired["aws_sdk_account.types.email_address.EmailAddress"]
    """<p>The email address associated with this alternate contact.</p>"""
    phone_number: NotRequired["aws_sdk_account.types.phone_number.PhoneNumber"]
    """<p>The phone number associated with this alternate contact.</p>"""
    alternate_contact_type: NotRequired[
        "aws_sdk_account.types.alternate_contact_type.AlternateContactType"
    ]
    """<p>The type of alternate contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlternateContact) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "title" in value:
        out["Title"] = value["title"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "alternate_contact_type" in value:
        out["AlternateContactType"] = value["alternate_contact_type"]
    return out


def deserialize_json(data: dict) -> AlternateContact:
    out: AlternateContact = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "AlternateContactType" in data:
        out["alternate_contact_type"] = data["AlternateContactType"]
    return out
