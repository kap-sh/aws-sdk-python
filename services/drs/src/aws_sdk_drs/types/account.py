"""Generated from Smithy shape ``com.amazonaws.drs#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id


class Account(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_drs.types.account_id.AccountID"]
    """<p>Account ID of AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
