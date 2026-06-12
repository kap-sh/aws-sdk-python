"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainDeliverabilityCampaign``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.campaign_id
    import aws_sdk_sesv2.types.esps
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.image_url
    import aws_sdk_sesv2.types.ip_list
    import aws_sdk_sesv2.types.percentage
    import aws_sdk_sesv2.types.subject
    import aws_sdk_sesv2.types.timestamp
    import aws_sdk_sesv2.types.volume


class DomainDeliverabilityCampaign(TypedDict):
    campaign_id: NotRequired["aws_sdk_sesv2.types.campaign_id.CampaignId"]
    """<p>The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.</p>"""
    image_url: NotRequired["aws_sdk_sesv2.types.image_url.ImageUrl"]
    """<p>The URL of an image that contains a snapshot of the email message that was sent.</p>"""
    subject: NotRequired["aws_sdk_sesv2.types.subject.Subject"]
    """<p>The subject line, or title, of the email message.</p>"""
    from_address: NotRequired["aws_sdk_sesv2.types.identity.Identity"]
    """<p>The verified email address that the email message was sent from.</p>"""
    sending_ips: NotRequired["aws_sdk_sesv2.types.ip_list.IpList"]
    """<p>The IP addresses that were used to send the email message.</p>"""
    first_seen_date_time: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The first time when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.</p>"""
    last_seen_date_time: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The last time when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.</p>"""
    inbox_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The number of email messages that were delivered to recipients’ inboxes.</p>"""
    spam_count: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The number of email messages that were delivered to recipients' spam or junk mail folders.</p>"""
    read_rate: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of email messages that were opened by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.</p>"""
    delete_rate: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of email messages that were deleted by recipients, without being opened first. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.</p>"""
    read_delete_rate: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of email messages that were opened and then deleted by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.</p>"""
    projected_volume: NotRequired["aws_sdk_sesv2.types.volume.Volume"]
    """<p>The projected number of recipients that the email message was sent to.</p>"""
    esps: NotRequired["aws_sdk_sesv2.types.esps.Esps"]
    """<p>The major email providers who handled the email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityCampaign) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "sending_ips" in value:
        import aws_sdk_sesv2.types.ip_list

        out["SendingIps"] = aws_sdk_sesv2.types.ip_list.serialize_json(
            value["sending_ips"]
        )
    if "first_seen_date_time" in value:
        import aws_sdk_sesv2.types.timestamp

        out["FirstSeenDateTime"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["first_seen_date_time"]
        )
    if "last_seen_date_time" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastSeenDateTime"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_seen_date_time"]
        )
    if "inbox_count" in value:
        out["InboxCount"] = value["inbox_count"]
    if "spam_count" in value:
        out["SpamCount"] = value["spam_count"]
    if "read_rate" in value:
        out["ReadRate"] = value["read_rate"]
    if "delete_rate" in value:
        out["DeleteRate"] = value["delete_rate"]
    if "read_delete_rate" in value:
        out["ReadDeleteRate"] = value["read_delete_rate"]
    if "projected_volume" in value:
        out["ProjectedVolume"] = value["projected_volume"]
    if "esps" in value:
        import aws_sdk_sesv2.types.esps

        out["Esps"] = aws_sdk_sesv2.types.esps.serialize_json(value["esps"])
    return out


def deserialize_json(data: dict) -> DomainDeliverabilityCampaign:
    out: DomainDeliverabilityCampaign = {}  # type: ignore[typeddict-item]
    if "CampaignId" in data:
        out["campaign_id"] = data["CampaignId"]
    if "ImageUrl" in data:
        out["image_url"] = data["ImageUrl"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "FromAddress" in data:
        out["from_address"] = data["FromAddress"]
    if "SendingIps" in data:
        import aws_sdk_sesv2.types.ip_list

        out["sending_ips"] = aws_sdk_sesv2.types.ip_list.deserialize_json(
            data["SendingIps"]
        )
    if "FirstSeenDateTime" in data:
        import aws_sdk_sesv2.types.timestamp

        out["first_seen_date_time"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["FirstSeenDateTime"]
        )
    if "LastSeenDateTime" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_seen_date_time"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastSeenDateTime"]
        )
    if "InboxCount" in data:
        out["inbox_count"] = data["InboxCount"]
    if "SpamCount" in data:
        out["spam_count"] = data["SpamCount"]
    if "ReadRate" in data:
        out["read_rate"] = data["ReadRate"]
    if "DeleteRate" in data:
        out["delete_rate"] = data["DeleteRate"]
    if "ReadDeleteRate" in data:
        out["read_delete_rate"] = data["ReadDeleteRate"]
    if "ProjectedVolume" in data:
        out["projected_volume"] = data["ProjectedVolume"]
    if "Esps" in data:
        import aws_sdk_sesv2.types.esps

        out["esps"] = aws_sdk_sesv2.types.esps.deserialize_json(data["Esps"])
    return out
