"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageTopAccountResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.total


class UsageTopAccountResult(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The unique account ID.</p>"""
    total: NotRequired["capo_guardduty.types.total.Total"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTopAccountResult) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "total" in value:
        import capo_guardduty.types.total

        out["total"] = capo_guardduty.types.total.serialize_json(value["total"])
    return out


def deserialize_json(data: dict) -> UsageTopAccountResult:
    out: UsageTopAccountResult = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "total" in data:
        import capo_guardduty.types.total

        out["total"] = capo_guardduty.types.total.deserialize_json(data["total"])
    return out
