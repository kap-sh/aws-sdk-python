"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageTopAccountResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.total


class UsageTopAccountResult(TypedDict):
    account_id: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The unique account ID.</p>"""
    total: NotRequired["aws_sdk_guardduty.types.total.Total"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTopAccountResult) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "total" in value:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.serialize_json(value["total"])
    return out


def deserialize_json(data: dict) -> UsageTopAccountResult:
    out: UsageTopAccountResult = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "total" in data:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.deserialize_json(data["total"])
    return out
