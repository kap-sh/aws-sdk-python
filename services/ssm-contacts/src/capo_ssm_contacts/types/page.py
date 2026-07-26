"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Page``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.sender
    import capo_ssm_contacts.types.ssm_contacts_arn


class Page(TypedDict, closed=True):
    page_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the page to the contact channel.</p>"""
    engagement_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the engagement that this page is part of.</p>"""
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that Incident Manager is engaging.</p>"""
    sender: "capo_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    incident_id: NotRequired["capo_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that's engaging the contact channel.</p>"""
    sent_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that Incident Manager engaged the contact channel.</p>"""
    delivery_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time the message was delivered to the contact channel.</p>"""
    read_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the contact channel acknowledged engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Page) -> dict:
    out: dict = {}
    out["PageArn"] = value["page_arn"]
    out["EngagementArn"] = value["engagement_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Sender"] = value["sender"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "sent_time" in value:
        import capo_ssm_contacts.types.date_time

        out["SentTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["sent_time"]
        )
    if "delivery_time" in value:
        import capo_ssm_contacts.types.date_time

        out["DeliveryTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["delivery_time"]
        )
    if "read_time" in value:
        import capo_ssm_contacts.types.date_time

        out["ReadTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["read_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Page:
    out: Page = {}  # type: ignore[typeddict-item]
    if "PageArn" in data:
        out["page_arn"] = data["PageArn"]
    else:
        raise DeserializationError("Page.page_arn required")
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        raise DeserializationError("Page.engagement_arn required")
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("Page.contact_arn required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("Page.sender required")
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "SentTime" in data:
        import capo_ssm_contacts.types.date_time

        out["sent_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["SentTime"]
        )
    if "DeliveryTime" in data:
        import capo_ssm_contacts.types.date_time

        out["delivery_time"] = (
            capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["DeliveryTime"]
            )
        )
    if "ReadTime" in data:
        import capo_ssm_contacts.types.date_time

        out["read_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["ReadTime"]
        )
    return out
