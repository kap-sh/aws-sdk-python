"""Generated from Smithy shape ``com.amazonaws.securityhub#AccountDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_id
    import aws_sdk_securityhub.types.non_empty_string


class AccountDetails(TypedDict):
    account_id: NotRequired["aws_sdk_securityhub.types.account_id.AccountId"]
    """<p>The ID of an Amazon Web Services account.</p>"""
    email: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The email of an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetails) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_json(data: dict) -> AccountDetails:
    out: AccountDetails = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Email" in data:
        out["email"] = data["Email"]
    return out
