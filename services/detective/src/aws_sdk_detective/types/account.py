"""Generated from Smithy shape ``com.amazonaws.detective#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id
    import aws_sdk_detective.types.email_address


class Account(TypedDict, closed=True):
    account_id: "aws_sdk_detective.types.account_id.AccountId"
    """<p>The account identifier of the Amazon Web Services account.</p>"""
    email_address: "aws_sdk_detective.types.email_address.EmailAddress"
    """<p>The Amazon Web Services account root user email address for the Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("Account.account_id required")
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("Account.email_address required")
    return out
