"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DescribePageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.content
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.incident_id
    import aws_sdk_ssm_contacts.types.public_content
    import aws_sdk_ssm_contacts.types.public_subject
    import aws_sdk_ssm_contacts.types.sender
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.subject


class DescribePageResult(TypedDict, closed=True):
    page_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement to a contact channel.</p>"""
    engagement_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the engagement that engaged the contact channel.</p>"""
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that was engaged.</p>"""
    sender: "aws_sdk_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    subject: "aws_sdk_ssm_contacts.types.subject.Subject"
    """<p>The secure subject of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> and <code>EMAIL</code>.</p>"""
    content: "aws_sdk_ssm_contacts.types.content.Content"
    """<p>The secure content of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> and <code>EMAIL</code>.</p>"""
    public_subject: NotRequired[
        "aws_sdk_ssm_contacts.types.public_subject.PublicSubject"
    ]
    """<p>The insecure subject of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    public_content: NotRequired[
        "aws_sdk_ssm_contacts.types.public_content.PublicContent"
    ]
    """<p>The insecure content of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    incident_id: NotRequired["aws_sdk_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that engaged the contact channel.</p>"""
    sent_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The time the engagement was sent to the contact channel.</p>"""
    read_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the contact channel acknowledged the engagement.</p>"""
    delivery_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the contact channel received the engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePageResult) -> dict:
    out: dict = {}
    out["PageArn"] = value["page_arn"]
    out["EngagementArn"] = value["engagement_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Sender"] = value["sender"]
    out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    if "public_subject" in value:
        out["PublicSubject"] = value["public_subject"]
    if "public_content" in value:
        out["PublicContent"] = value["public_content"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "sent_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["SentTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["sent_time"]
        )
    if "read_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["ReadTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["read_time"]
        )
    if "delivery_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["DeliveryTime"] = (
            aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
                value["delivery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePageResult:
    out: DescribePageResult = {}  # type: ignore[typeddict-item]
    if "PageArn" in data:
        out["page_arn"] = data["PageArn"]
    else:
        raise DeserializationError("DescribePageResult.page_arn required")
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        raise DeserializationError("DescribePageResult.engagement_arn required")
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("DescribePageResult.contact_arn required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("DescribePageResult.sender required")
    if "Subject" in data:
        out["subject"] = data["Subject"]
    else:
        raise DeserializationError("DescribePageResult.subject required")
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("DescribePageResult.content required")
    if "PublicSubject" in data:
        out["public_subject"] = data["PublicSubject"]
    if "PublicContent" in data:
        out["public_content"] = data["PublicContent"]
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "SentTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["sent_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["SentTime"]
            )
        )
    if "ReadTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["read_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["ReadTime"]
            )
        )
    if "DeliveryTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["delivery_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["DeliveryTime"]
            )
        )
    return out
