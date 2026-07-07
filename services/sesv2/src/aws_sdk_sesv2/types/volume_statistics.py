"""Generated from Smithy shape ``com.amazonaws.sesv2#VolumeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.volume


class VolumeStatistics(TypedDict, closed=True):
    inbox_raw_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The total number of emails that arrived in recipients' inboxes.</p>"""
    spam_raw_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The total number of emails that arrived in recipients' spam or junk mail folders.</p>"""
    projected_inbox: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>An estimate of the percentage of emails sent from the current domain that will arrive in recipients' inboxes.</p>"""
    projected_spam: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>An estimate of the percentage of emails sent from the current domain that will arrive in recipients' spam or junk mail folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeStatistics) -> dict:
    out: dict = {}
    if "inbox_raw_count" in value:
        out["InboxRawCount"] = value["inbox_raw_count"]
    if "spam_raw_count" in value:
        out["SpamRawCount"] = value["spam_raw_count"]
    if "projected_inbox" in value:
        out["ProjectedInbox"] = value["projected_inbox"]
    if "projected_spam" in value:
        out["ProjectedSpam"] = value["projected_spam"]
    return out


def deserialize_json(data: dict) -> VolumeStatistics:
    out: VolumeStatistics = {}  # type: ignore[typeddict-item]
    if "InboxRawCount" in data:
        out["inbox_raw_count"] = data["InboxRawCount"]
    if "SpamRawCount" in data:
        out["spam_raw_count"] = data["SpamRawCount"]
    if "ProjectedInbox" in data:
        out["projected_inbox"] = data["ProjectedInbox"]
    if "ProjectedSpam" in data:
        out["projected_spam"] = data["ProjectedSpam"]
    return out
