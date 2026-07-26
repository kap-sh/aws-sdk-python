"""Generated from Smithy shape ``com.amazonaws.guardduty#UnprocessedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.string


class UnprocessedAccount(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    result: NotRequired["capo_guardduty.types.string.String"]
    """<p>A reason why the account hasn't been processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "result" in value:
        out["result"] = value["result"]
    return out


def deserialize_json(data: dict) -> UnprocessedAccount:
    out: UnprocessedAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "result" in data:
        out["result"] = data["result"]
    return out
