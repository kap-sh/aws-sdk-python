"""Generated from Smithy shape ``com.amazonaws.detective#UnprocessedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id
    import aws_sdk_detective.types.unprocessed_reason


class UnprocessedAccount(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_detective.types.account_id.AccountId"]
    """<p>The Amazon Web Services account identifier of the member account that was not processed.</p>"""
    reason: NotRequired["aws_sdk_detective.types.unprocessed_reason.UnprocessedReason"]
    """<p>The reason that the member account request could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedAccount:
    out: UnprocessedAccount = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
