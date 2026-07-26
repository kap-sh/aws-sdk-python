"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PlacementStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.percentage


class PlacementStatistics(TypedDict, closed=True):
    inbox_percentage: NotRequired["capo_pinpoint_email.types.percentage.Percentage"]
    """<p>The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.</p>"""
    spam_percentage: NotRequired["capo_pinpoint_email.types.percentage.Percentage"]
    """<p>The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.</p>"""
    missing_percentage: NotRequired["capo_pinpoint_email.types.percentage.Percentage"]
    """<p>The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.</p>"""
    spf_percentage: NotRequired["capo_pinpoint_email.types.percentage.Percentage"]
    """<p>The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.</p>"""
    dkim_percentage: NotRequired["capo_pinpoint_email.types.percentage.Percentage"]
    """<p>The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlacementStatistics) -> dict:
    out: dict = {}
    if "inbox_percentage" in value:
        out["InboxPercentage"] = value["inbox_percentage"]
    if "spam_percentage" in value:
        out["SpamPercentage"] = value["spam_percentage"]
    if "missing_percentage" in value:
        out["MissingPercentage"] = value["missing_percentage"]
    if "spf_percentage" in value:
        out["SpfPercentage"] = value["spf_percentage"]
    if "dkim_percentage" in value:
        out["DkimPercentage"] = value["dkim_percentage"]
    return out


def deserialize_json(data: dict) -> PlacementStatistics:
    out: PlacementStatistics = {}  # type: ignore[typeddict-item]
    if "InboxPercentage" in data:
        out["inbox_percentage"] = data["InboxPercentage"]
    if "SpamPercentage" in data:
        out["spam_percentage"] = data["SpamPercentage"]
    if "MissingPercentage" in data:
        out["missing_percentage"] = data["MissingPercentage"]
    if "SpfPercentage" in data:
        out["spf_percentage"] = data["SpfPercentage"]
    if "DkimPercentage" in data:
        out["dkim_percentage"] = data["DkimPercentage"]
    return out
