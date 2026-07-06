"""Generated from Smithy shape ``com.amazonaws.mgn#ManagedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id


class ManagedAccount(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Managed account, account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ManagedAccount:
    out: ManagedAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
