"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class AccountStatistics(TypedDict):
    account_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    last_generated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the finding for this account was last generated.</p>"""
    total_findings: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The total number of findings associated with an account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountStatistics) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "last_generated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["lastGeneratedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["last_generated_at"]
        )
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    return out


def deserialize_json(data: dict) -> AccountStatistics:
    out: AccountStatistics = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "lastGeneratedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["last_generated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["lastGeneratedAt"]
        )
    if "totalFindings" in data:
        out["total_findings"] = data["totalFindings"]
    return out
