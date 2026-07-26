"""Generated from Smithy shape ``com.amazonaws.sso#AccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso.types.account_id_type
    import capo_sso.types.account_name_type
    import capo_sso.types.email_address_type


class AccountInfo(TypedDict, closed=True):
    account_id: NotRequired["capo_sso.types.account_id_type.AccountIdType"]
    """<p>The identifier of the AWS account that is assigned to the user.</p>"""
    account_name: NotRequired["capo_sso.types.account_name_type.AccountNameType"]
    """<p>The display name of the AWS account that is assigned to the user.</p>"""
    email_address: NotRequired["capo_sso.types.email_address_type.EmailAddressType"]
    """<p>The email address of the AWS account that is assigned to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> AccountInfo:
    out: AccountInfo = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "accountName" in data:
        out["account_name"] = data["accountName"]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    return out
