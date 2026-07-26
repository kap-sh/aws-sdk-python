"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DescribeEngagementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.content
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.public_content
    import capo_ssm_contacts.types.public_subject
    import capo_ssm_contacts.types.sender
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.subject


class DescribeEngagementResult(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the escalation plan or contacts involved in the engagement.</p>"""
    engagement_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the engagement.</p>"""
    sender: "capo_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    subject: "capo_ssm_contacts.types.subject.Subject"
    """<p>The secure subject of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> and <code>EMAIL</code>.</p>"""
    content: "capo_ssm_contacts.types.content.Content"
    """<p>The secure content of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> and <code>EMAIL</code>.</p>"""
    public_subject: NotRequired["capo_ssm_contacts.types.public_subject.PublicSubject"]
    """<p>The insecure subject of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    public_content: NotRequired["capo_ssm_contacts.types.public_content.PublicContent"]
    """<p>The insecure content of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    incident_id: NotRequired["capo_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident in which the engagement occurred.</p>"""
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement started.</p>"""
    stop_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement ended.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngagementResult) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["EngagementArn"] = value["engagement_arn"]
    out["Sender"] = value["sender"]
    out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    if "public_subject" in value:
        out["PublicSubject"] = value["public_subject"]
    if "public_content" in value:
        out["PublicContent"] = value["public_content"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "start_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "stop_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StopTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["stop_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngagementResult:
    out: DescribeEngagementResult = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("DescribeEngagementResult.contact_arn required")
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        raise DeserializationError("DescribeEngagementResult.engagement_arn required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("DescribeEngagementResult.sender required")
    if "Subject" in data:
        out["subject"] = data["Subject"]
    else:
        raise DeserializationError("DescribeEngagementResult.subject required")
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("DescribeEngagementResult.content required")
    if "PublicSubject" in data:
        out["public_subject"] = data["PublicSubject"]
    if "PublicContent" in data:
        out["public_content"] = data["PublicContent"]
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "StartTime" in data:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "StopTime" in data:
        import capo_ssm_contacts.types.date_time

        out["stop_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StopTime"]
        )
    return out
