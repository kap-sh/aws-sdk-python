"""Generated from Smithy shape ``com.amazonaws.devopsguru#AccountHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.account_insight_health
    import capo_devops_guru.types.aws_account_id


class AccountHealth(TypedDict, closed=True):
    account_id: NotRequired["capo_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account. </p>"""
    insight: NotRequired[
        "capo_devops_guru.types.account_insight_health.AccountInsightHealth"
    ]
    """<p> Information about the health of the Amazon Web Services resources in your account, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountHealth) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "insight" in value:
        import capo_devops_guru.types.account_insight_health

        out["Insight"] = capo_devops_guru.types.account_insight_health.serialize_json(
            value["insight"]
        )
    return out


def deserialize_json(data: dict) -> AccountHealth:
    out: AccountHealth = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Insight" in data:
        import capo_devops_guru.types.account_insight_health

        out["insight"] = capo_devops_guru.types.account_insight_health.deserialize_json(
            data["Insight"]
        )
    return out
