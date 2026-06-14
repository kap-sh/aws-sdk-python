"""Generated from Smithy shape ``com.amazonaws.account#PutAlternateContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_account.types.account_id
    import aws_sdk_account.types.alternate_contact_type
    import aws_sdk_account.types.email_address
    import aws_sdk_account.types.name
    import aws_sdk_account.types.phone_number
    import aws_sdk_account.types.title


class PutAlternateContactRequest(TypedDict):
    name: "aws_sdk_account.types.name.Name"
    """<p>Specifies a name for the alternate contact.</p>"""
    title: "aws_sdk_account.types.title.Title"
    """<p>Specifies a title for the alternate contact.</p>"""
    email_address: "aws_sdk_account.types.email_address.EmailAddress"
    """<p>Specifies an email address for the alternate contact. </p>"""
    phone_number: "aws_sdk_account.types.phone_number.PhoneNumber"
    """<p>Specifies a phone number for the alternate contact.</p>"""
    alternate_contact_type: (
        "aws_sdk_account.types.alternate_contact_type.AlternateContactType"
    )
    """<p>Specifies which alternate contact you want to create or update.</p>"""
    account_id: NotRequired["aws_sdk_account.types.account_id.AccountId"]
    r"""<p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAlternateContactRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Title"] = value["title"]
    out["EmailAddress"] = value["email_address"]
    out["PhoneNumber"] = value["phone_number"]
    out["AlternateContactType"] = value["alternate_contact_type"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PutAlternateContactRequest:
    out: PutAlternateContactRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutAlternateContactRequest.name required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("PutAlternateContactRequest.title required")
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("PutAlternateContactRequest.email_address required")
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("PutAlternateContactRequest.phone_number required")
    if "AlternateContactType" in data:
        out["alternate_contact_type"] = data["AlternateContactType"]
    else:
        raise DeserializationError(
            "PutAlternateContactRequest.alternate_contact_type required"
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
