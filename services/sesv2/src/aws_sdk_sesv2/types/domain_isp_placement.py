"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainIspPlacement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.isp_name
    import aws_sdk_sesv2.types.percentage
    import aws_sdk_sesv2.types.volume


class DomainIspPlacement(TypedDict):
    isp_name: NotRequired["aws_sdk_sesv2.types.isp_name.IspName"]
    """<p>The name of the email provider that the inbox placement data applies to.</p>"""
    inbox_raw_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.</p>"""
    spam_raw_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.</p>"""
    inbox_percentage: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.</p>"""
    spam_percentage: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainIspPlacement) -> dict:
    out: dict = {}
    if "isp_name" in value:
        out["IspName"] = value["isp_name"]
    if "inbox_raw_count" in value:
        out["InboxRawCount"] = value["inbox_raw_count"]
    if "spam_raw_count" in value:
        out["SpamRawCount"] = value["spam_raw_count"]
    if "inbox_percentage" in value:
        out["InboxPercentage"] = value["inbox_percentage"]
    if "spam_percentage" in value:
        out["SpamPercentage"] = value["spam_percentage"]
    return out


def deserialize_json(data: dict) -> DomainIspPlacement:
    out: DomainIspPlacement = {}  # type: ignore[typeddict-item]
    if "IspName" in data:
        out["isp_name"] = data["IspName"]
    if "InboxRawCount" in data:
        out["inbox_raw_count"] = data["InboxRawCount"]
    if "SpamRawCount" in data:
        out["spam_raw_count"] = data["SpamRawCount"]
    if "InboxPercentage" in data:
        out["inbox_percentage"] = data["InboxPercentage"]
    if "SpamPercentage" in data:
        out["spam_percentage"] = data["SpamPercentage"]
    return out
