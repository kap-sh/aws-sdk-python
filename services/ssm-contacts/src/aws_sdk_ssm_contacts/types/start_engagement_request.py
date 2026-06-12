"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StartEngagementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.content
    import aws_sdk_ssm_contacts.types.idempotency_token
    import aws_sdk_ssm_contacts.types.incident_id
    import aws_sdk_ssm_contacts.types.public_content
    import aws_sdk_ssm_contacts.types.public_subject
    import aws_sdk_ssm_contacts.types.sender
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.subject


class StartEngagementRequest(TypedDict):
    contact_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact being engaged.</p>"""
    sender: "aws_sdk_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    subject: "aws_sdk_ssm_contacts.types.subject.Subject"
    """<p>The secure subject of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>"""
    content: "aws_sdk_ssm_contacts.types.content.Content"
    """<p>The secure content of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>"""
    public_subject: NotRequired[
        "aws_sdk_ssm_contacts.types.public_subject.PublicSubject"
    ]
    """<p>The insecure subject of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    public_content: NotRequired[
        "aws_sdk_ssm_contacts.types.public_content.PublicContent"
    ]
    """<p>The insecure content of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    incident_id: NotRequired["aws_sdk_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that the engagement is part of.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEngagementRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["Sender"] = value["sender"]
    out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    if "public_subject" in value:
        out["PublicSubject"] = value["public_subject"]
    if "public_content" in value:
        out["PublicContent"] = value["public_content"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEngagementRequest:
    out: StartEngagementRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StartEngagementRequest.contact_id required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("StartEngagementRequest.sender required")
    if "Subject" in data:
        out["subject"] = data["Subject"]
    else:
        raise DeserializationError("StartEngagementRequest.subject required")
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("StartEngagementRequest.content required")
    if "PublicSubject" in data:
        out["public_subject"] = data["PublicSubject"]
    if "PublicContent" in data:
        out["public_content"] = data["PublicContent"]
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
