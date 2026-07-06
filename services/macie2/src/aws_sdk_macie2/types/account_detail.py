"""Generated from Smithy shape ``com.amazonaws.macie2#AccountDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class AccountDetail(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    email: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The email address for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetail) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> AccountDetail:
    out: AccountDetail = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "email" in data:
        out["email"] = data["email"]
    return out
