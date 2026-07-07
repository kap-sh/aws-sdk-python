"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Engagement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.incident_id
    import aws_sdk_ssm_contacts.types.sender
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class Engagement(TypedDict, closed=True):
    engagement_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement.</p>"""
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the escalation plan or contact that Incident Manager is engaging.</p>"""
    sender: "aws_sdk_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    incident_id: NotRequired["aws_sdk_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that's engaging the contact.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement began.</p>"""
    stop_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement ended.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Engagement) -> dict:
    out: dict = {}
    out["EngagementArn"] = value["engagement_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Sender"] = value["sender"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "stop_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StopTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["stop_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Engagement:
    out: Engagement = {}  # type: ignore[typeddict-item]
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        raise DeserializationError("Engagement.engagement_arn required")
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("Engagement.contact_arn required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("Engagement.sender required")
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "StopTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["stop_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StopTime"]
            )
        )
    return out
